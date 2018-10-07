#第二章
### 2.1 knn算法概述
采用测量不同特征值之间的距离方法进行分类

 - 优点：精度高、对异常值不敏感、无数据输入假定。 
 - 缺点：计算复杂度高、空间复杂度高。
 - 适用数据范围：数值型和标称型。

knn工作原理：存在一个样本数据集合，也称作训练样本集，并且样本集中每个数据都存在标签，即我们知道样本集中每一数据与所属分类的对应关系。输入没有标签的新数据后，将新数据的每个特征与样本集中数据对应的特征进行比较，然后算法提取样本集中特征最相似数据（最近邻）的分类标签，最后选择k个最相似数据中出现次数最多的分类，作为新数据的分类。

 - 通常k是不大于20的整数

示例代码

```
#创建数据集和标签
import operator
from numpy import *

def createData():
    group = array([[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels
```
```
#分类器
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    #距离计算
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat **2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    #选择距离最小的k个点
    classCount={}
    for j in labels:
        classCount[j] = 0
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    #排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
```
### 2.2 示例：使用k-近邻算法改进约会网站的配对效果
    
```
#将文本记录转换为Numpy
def file2matrix(filename):
    #文件行数
    fr = open(filename)
    arrayOlines = fr.readlines()
    numberOfLines = len(arrayOlines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    #解析文件数据到列表
    for line in arrayOlines:
        line = line.strip()
        listFromLine = line.split(' ')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector
```
```
#使用Matplotlib创建散点图
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0*array(datingLabels), 15.0*array(datingLabels))
plt.show()
```
 - 归一化数值：处理这种不同取值范围的特征值时所采用，将取值范围
处理为0到1或者-1到1之间，公式：newValue = (oldValue-min)/(max - min)
```
#归一化特征值
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    #tile()将变量内容复制成输入矩阵同样大小的矩阵
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet/tile(ranges, (m, 1))
    return normDataSet, ranges, minVals
```
```
#分类器针对约会网站的测试代码
def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("The classifier came back with %d, the real answer is : %d" %(classifierResult, datingLabels[i]))
        if(classifierResult != datingLabels[i]): errorCount += 1.0
    print("The total error rate is : %f" %(errorCount/float(numTestVecs)))
```

### 2.3 示例：手写识别系统
#### 详见 [Digit Recognizer][1]


  [1]: https://github.com/huangyt39/machine-learning/tree/master/Digit%20Recognizer