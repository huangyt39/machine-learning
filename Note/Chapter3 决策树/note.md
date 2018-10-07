#第三章
### 3.1 决策树的构造
1.决策树
 - 优点：计算复杂度不高，输出结果易于理解，对中间值的缺失不敏感，可以处理不相关特征数据。
 - 缺点：可能会产生过度匹配问题。
 - 适用数据类型：数值型和标称型。

2.信息增益
 - 信息：l(xi) = -log2p(xi)，其中p(xi)是选择该分类的概率
 - 香农熵/熵：信息的期望值, 熵越高，则混合的数据也越多
 - 所有类别所有可能值包含的信息期望值：H = -..

```
#计算给定数据集的香农熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt
#测试
def createDataSet():
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels
 ```
 ```
#按照给定特征划分数据集
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet
```
```
#选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain, bestFeature = 0.0, -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if infoGain >bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature
```
3.递归构建决策树
工作原理：对于原始数据集，基于最好的属性值进行划分(可能存在大于两个分支的数据集划分)。第一次划分之后，数据将被向下传递到树分支的下一个节点，在这个节点上，再次划分数据。
递归结束条件：程序遍历完所有划分数据集的属性，或者每个分支下的所有实例都具有相同的分类。
```
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortClassCount = sorted(classCount.items(), key=operator.itemgetter(1),reverse=True)
    return sortClassCount[0][0]

#创建树的函数代码
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree
```
```
#构造结果
{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
```

### 3.2 使用Matplotlib注解绘制树形图
1.注解
Matplotlib提供了一个注解工具annotations，可以在数据图形上添加文本注释。
```
#使用文本注解绘制树节点
import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle = "<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',\
    xytext=centerPt,textcoords='axes fraction',\
    va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)

def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotNode(U'决策节点', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode(U'叶节点', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()

if __name__ == "__main__":
    createPlot()
```
2.构造注解树
```
#获取叶节点的数目
def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs

#获取树的层数
def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in myTree.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth

#测试
def retrieveTree(i):
    listOfTrees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},\
    {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head':{0: 'no', 1:'yes'}}, 1: 'no'}}}}]
    return listOfTrees[i]
```
```
#在父子节点之间填充文本消息
def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0])/2.0 + cntrPt[0]
    yMid = (parentPt[0] - cntrPt[1])/2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString)

def plotTree(myTree, parentPt, nodeTxt):
    #计算宽高
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]
    cntrPt = (plotTree.x0ff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.y0ff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    #标记子节点属性值
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    #减少y偏移
    plotTree.y0ff = plotTree.y0ff - 1.0/plotTree.totalD
    for key in list(secondDict.keys()):
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key],cntrPt, str(key))
        else:
            plotTree.x0ff = plotTree.x0ff + 1.0/plotTree.totalW
            plotNode(secondDict[key], (plotTree.x0ff, plotTree.y0ff),cntrPt,leafNode)
            plotMidText((plotTree.x0ff, plotTree.y0ff),cntrPt,str(key))
    plotTree.y0ff = plotTree.y0ff + 1.0/plotTree.totalD

#创建绘图区，计算树形图的全局尺寸，并调用递归函数plotTree()
def createPlot(inTree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.x0ff, plotTree.y0ff = -0.5/plotTree.totalW, 1.0
    # plotNode(U'决策节点', (0.5, 0.1), (0.1, 0.5), decisionNode)
    # plotNode(U'叶节点', (0.8, 0.1), (0.3, 0.8), leafNode)
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()
```
测试结果
![树形图][1]

### 3.3 测试和存储分类器
1.使用决策树执行分类：
在执行数据分类时，需要决策树以及用于构造树的标签向量。然后，程序比较测试数据与决策树上的数值，递归执行该过程直到进入叶子节点；最后将测试数据定义为叶子节点所属的类型。
```
#使用决策树的分类函数
def classify(inputTree, featLabels, testVec):
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in list(secondDict.keys()):
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels,testVec)
            else:
                classLabel = secondDict[key]
    return classLabel
```
2.决策树的存储
构造决策树是很耗时的任务，即使处理很小的数据集，如前面的样本数据，也要花费几秒的时间，如果数据集很大，将会耗费很多计算时间。为了避免每次使用分类器时，必须重新构造决策树，应该在硬盘上存储决策树分类器。需要使用Python模块pickle序列化对象，任何对象都可以执行序列化操作，并在磁盘上保存对象。
```
#使用pickle模块存储决策树
def storeTree(inputTree,filename):
    import pickle
    fw = open(filename, 'wb')
    pickle.dump(inputTree, fw)
    fw.close()

def grabTree(filename):
    import pickle
    fr = open(filename, 'rb')
    return pickle.load(fr)

```
### 3.4 示例：使用决策树预测隐形眼镜类型
...
本章使用的算法称为ID3，它是一个好的算法但并不完美。ID3算法无法直接处理数值型数据，尽管我们可以通过量化的方法将数值型数据转化为标称型数值，但是如果存在太多的特征划分，ID3算法仍然会面临其他问题。
小结：
决策树分类器就像带有终止块的流程图，终止块表示分类结果。开始处理数据集时，我们首先需要测量集合中数据的不一致性，也就是熵，然后寻找最优方案划分数据集，直到数据集中的所有数据属于同一分类。ID3算法可以用于划分标称型数据集。
  [1]: https://img1.doubanio.com/view/status/m/public/07e1ee215973ee7.webp