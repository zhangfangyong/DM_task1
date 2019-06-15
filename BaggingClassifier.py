import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import warnings
warnings.filterwarnings("ignore")

class BaggingClassifier():
    def __init__(self, n_model=10):
        '''
        初始化函数
        '''
        #分类器的数量，默认为10
        self.n_model = n_model
        #用于保存模型的列表，训练好分类器后将对象append进去即可
        self.models = []

    def fit(self, feature, label):
        '''
        训练模型，请记得将模型保存至self.models
        :param feature: 训练集数据，类型为ndarray
        :param label: 训练集标签，类型为ndarray
        :return: None
        '''
        for i in range(self.n_model):
            temp = np.random.randint(0,len(feature),size=(1,len(feature)))
            fea = feature[temp[0]]
            lab = label[temp[0]]
            #train = SVC(kernel='poly',degree=1,gamma=2,coef0=2)    #分类器采用SVC
            train = DecisionTreeClassifier()                      #分类器采用决策树
            #train = KNeighborsClassifier(3)                       #分类器采用KNN
            train.fit(fea, lab)
            self.models.append(train)

    def predict(self, feature):
        '''
        :param feature: 测试集数据，类型为ndarray
        :return: 预测结果，类型为ndarray
        '''
        result = []
        temp = []
        for i in self.models:
            result.append(i.predict(feature))
        resultsum = np.sum(result,axis=0).tolist()
        for j in resultsum:
            if j >= self.n_model/2:
                temp.append(1)
            else:
                temp.append(0)
        return np.asarray(temp)