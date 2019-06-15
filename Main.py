import pandas as pd
import numpy as np
from BaggingClassifier import BaggingClassifier


Data = []
Lable = []
#file = open('promoters.data', 'r', encoding='utf-8')   #运行原始数据集
file = open('chuli.txt', 'r', encoding='GBK')           #运行扩展数据集
fea= pd.read_csv('feature.csv',header=0)                #运行特征向量数据集
dev_fea = pd.read_csv('fea.csv',header=0)                     #运行扩展特征向量数据集
fileline = file.readline()
m = dev_fea.columns.size
fea_da = fea.values[:,1:m]
dev_fea_da = dev_fea.values[:,1:m]
while (fileline):
    fileline_A = fileline[0].rstrip("\n")
    fileline_A = fileline_A.replace('+',str(1))
    fileline_A = fileline_A.replace('-',str(0))
    fileline_A = list(map(int,fileline_A))

    fileline_D = fileline[len(fileline) - 58:].rstrip("\n")       #运行原始，扩展特征，特征数据集
    #fileline_D = fileline[2:116].rstrip("\n")                    #运行扩展数据集
    fileline_D = fileline_D.replace('a', str(1))
    fileline_D = fileline_D.replace('g', str(2))
    fileline_D = fileline_D.replace('c', str(3))
    fileline_D = fileline_D.replace('t', str(4))
    fileline_D = list(map(int,fileline_D))
    Lable.append(fileline_A)
    Data.append(fileline_D)
    fileline = file.readline()
Data = list(dev_fea_da)        #运行扩展特征数据集
#Data= list(fea_da)             #运行特征数据集
train_data = Data[0:40] + Data[53:93]
train_lable = Lable[0:40] + Lable[53:93]

test_data = Data[40:53] + Data[93:106]
test_lable = Lable[40:53] + Lable[93:106]

train_data = np.asarray(train_data)
train_lable = np.asarray(train_lable)
test_data = np.asarray(test_data)
test_lable = np.asarray(test_lable)

#调用Bagging方法
bagging = BaggingClassifier(10)
bagging.fit(train_data, train_lable)
predicted_labels = bagging.predict(test_data)

pre = pd.DataFrame(predicted_labels,columns=["result"])
pre.to_csv('result.csv')

correct = 0
for i in range(len(test_data)):
    if(predicted_labels[i] == test_lable[i]):
        correct += 1

#输出结果
correct_ratio = correct / len(test_data)
print("正确率为：", correct_ratio, end='')
