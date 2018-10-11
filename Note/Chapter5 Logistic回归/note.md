# 第五章 Logistic回归
回归：假设现在有一些数据点，我们用一条直线对这些点进行拟合（该线称为最佳拟合直线）这个拟合过程就称作回归。
### 5.1基于Logistic回归和Sigmoid函数的分类
Logistic回归
 - 优点：计算代价不高，易于理解和实现。
 - 缺点：容易欠拟合，分类精度可能不高。
 - 适用数据类型：数值型和标称型数据。
Sigmoid函数：
用Sigmoid函数实现Logistic回归分类器：
在每个特征上都乘以一个回归系数，然后把所有的结果值相加，将这个总和代入Sigmoid函数中，进而得到一个范围在0~1之间的值。再确定最佳回归系数
### 5.2 基于最优化方法的最佳回归系数确定
Sigmoid函数的输入记为z，z = w0x0 + w1x1 + w2x2 +...+ wnxn，向量x是分类器的输入数据，向量w也就是我们要找到的最佳参数(系数)
1.梯度上升法(求函数最大值)
基干思想：要找到某函数的最大值，最好的方法是沿着该函数的梯度方向探寻。
https://img1.doubanio.com/view/status/m/public/7396ea56b2b06dc.webp
2.使用梯度上升找到最佳参数
梯度上升伪代码：
每个回归系数初始化为1
重复R次：
    计算整个数据集的梯度
    使用alpha × gradient更新回归系数的向量
    返回回归系数
```
Logistic回归梯度上升优化算法
from numpy import *

#打开读取文件
def loadDataSet():
    dataMat, labelMat = [], []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat

def sigmoid(inX):
    return 1.0/(1+exp(-inX))

#梯度上升算法
def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).T
    m,n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n, 1))
    for k in range(maxCycles):
        #变量h不是一个数而是一个列向量，列向量的元素个数等于样本个数
        h = sigmoid(dataMatrix*weights)
        error = (labelMat - h)
        weights = weights + alpha*dataMatrix.T*error
    return weights

#画出数据集和Logistic回归最佳拟合直线的函数
def plotBestFit(wei):
    import matplotlib.pyplot as plt
    weights = wei
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1, ycord1, xcord2, ycord2 = [], [], [], []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red',marker='s')
    ax.scatter(xcord1, ycord1, s=30, c='g')
    #最佳拟合直线
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()
```
3.随机梯度上升
梯度上升算法的缺点：在每次更新回归系数时都需要遍历整个数据集，若数据集较大，计算复杂度太高。
改进：随机梯度上升，在新样本到来时对分类器进行增量式更新。
随机梯度上升伪代码：
    所有回归系数初始化为1
    对数据集中每个样本
        计算该样本的梯度
        使用alpha × gradient更新回归系数值
    返回回归系数值
```
#随机梯度上升算法
def stocGradAscent0(dataMatrix, classLabels):
    m,n = shape(dataMatrix)
    alpha = 0.01
    weights = ones(n)
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i]*weights))
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMatrix[i]
    return weights
```
随机梯度上升的缺点：需要较多的迭代才能达到稳定值。且存在一些不能正确分类的样本点（数据集并非线性可分），在每次迭代时会引发系数的剧烈改变。
```
#改进的随机梯度上升算法
def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    m,n = shape(dataMatrix)
    weights = ones(n)
    for j in range(numIter):
        dataIndex = range(m)
        for i in range(m):
            #alpha在每次迭代的时候都会调整，缓解数据波动
            alpha = 4/(1.0+j+i)+0.01
            #这里通过随机选取样本来更新回归系数，减少周期性波动
            randIndex = int(random.uniform(0, len(dataIndex)))
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights
```

### 5.3 示例：从疝气病症预测病马的死亡率
数据来源：http://archive.ics.uci.edu/ml/machine-learning-databases/horse-colic/
1.处理数据中的缺失值
回归系数的更新公式如下：
weights = weights + alpha * error *dataMatrix[randIndex]
故如果dataMatrix的某特征对应值为0，那么该特征的系数将不做更新,所以可以将缺失值用0代替
2.回归分类代码
```
def classifyVector(inX, weights):
    prob = sigmoid(sum(inX*weights))
    if prob > 0.5:
        return 1.0
    else:
        return 0.0

def colicTest():
    frTrain = open('horseColicTraining.txt')
    frTest = open('horseColicTest.txt')
    trainingSet, trainingLabels = [], []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(32):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    trainWeights = stocGradAscent1(array(trainingSet), trainingLabels, 500)
    errorCount, numTestVec = 0, 0.0
    for line in frTest.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(array(lineArr), trainWeights)) != int(currLine[21]):
            errorCount += 1
    errorRate = (float(errorCount/numTestVec))
    print("The error rate of this test is : %f" %errorRate)
    return errorRate

def multiTest():
    numTests, errorSum = 10, 0.0
    for k in range(numTests):
        errorSum += colicTest()
    print("After %d iterations the average error rate is: %f" %(numTests, errorSum/float(numTests)))
    
```