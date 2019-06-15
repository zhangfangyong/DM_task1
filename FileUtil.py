'''
#***********数据文件预处理**********#
#对数据和标签进行提取，重新生成相应的训练数据集，训练标签集，测试数据集，测试标签集
#共有106条数据，按照80：26的比例产生训练数据集和测试数据集
#文件保存格式csv
'''
import pandas as pd
import numpy as np

'''*********获取一般数据集**********'''
file = open('promoters.data', 'r', encoding='utf-8')
fileline = file.readline()
Data = []
Lable = []
while (fileline):
    fileline_A = fileline[0].rstrip("\n")
    fileline_A = fileline_A.replace('+',str(1))
    fileline_A = fileline_A.replace('-',str(0))
    fileline_A = list(map(int,fileline_A))

    fileline_D = fileline[len(fileline) - 58:].rstrip("\n")
    fileline_D = fileline_D.replace('a', str(1))
    fileline_D = fileline_D.replace('g', str(2))
    fileline_D = fileline_D.replace('c', str(3))
    fileline_D = fileline_D.replace('t', str(4))
    fileline_D = list(map(int,fileline_D))
    Lable.append(fileline_A)
    Data.append(fileline_D)
    fileline = file.readline()
save = pd.DataFrame(Data[0:40]+Data[53:93])
save.to_csv('train_data.csv')
save = pd.DataFrame(Lable[0:40]+Lable[53:93])
save.to_csv('train_lable.csv')
save = pd.DataFrame(Data[41:52]+Data[94:106])
save.to_csv('test_data.csv')
save = pd.DataFrame(Lable[41:52]+Lable[94:106])
save.to_csv('test_lable.csv')

'''*******获取自己构造的特征向量数据集*******'''
temp =[]
for t1 in 'agct':
    for t2 in 'agct':
        for t3 in 'agct':
            for t4 in 'agct':
                temp.append(t1+t2+t3+t4)
file = open('promoters.data', 'r', encoding='utf-8')
fileline = file.readline()
feature = []
jie = pd.DataFrame(columns=temp)
while(fileline):
    for i in temp:
        feature.append(fileline.count(i))
    t = pd.DataFrame([feature],columns=temp)
    jie = jie.append(t,ignore_index=True)
    feature.clear()
    fileline = file.readline()
jie.to_csv('feature.csv')

'''*******构造扩展数据集********'''
file = open('promoters.data', 'r', encoding='utf-8')
fileline = file.readline()
temp = []
while(fileline):
    temp.append(fileline[len(fileline) - 58:].rstrip("\n"))
    fileline = file.readline()
str = []
for i in range(len(temp)):
    if i == 52:
        str.append(temp[i]+temp[0])
    elif i == 105:
        str.append(temp[i]+temp[53])
    else:
        str.append(temp[i]+temp[i+1])
save = pd.DataFrame(str)
save.to_csv('chuli.csv')

'''********构造扩展特征数据集***********'''
temp =[]
for t1 in 'agct':
    for t2 in 'agct':
        for t3 in 'agct':
            for t4 in 'agct':
                temp.append(t1+t2+t3+t4)
file = open('chuli.txt', 'r', encoding='utf-8')
fileline = file.readline()
feature = []
jie = pd.DataFrame(columns=temp)
while(fileline):
    for i in temp:
        feature.append(fileline.count(i))
    t = pd.DataFrame([feature],columns=temp)
    jie = jie.append(t,ignore_index=True)
    feature.clear()
    fileline = file.readline()
jie.to_csv('fea.csv')
