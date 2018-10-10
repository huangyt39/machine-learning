## 画出不同分类坐标的边界

### 给定数据的散点图如下
不同颜色代表不同分类
![给定数据][1]

### 解决方案
将给定数据作为训练集，生成1000000个坐标数据作为测试集，用knn（k=1）算法算出测试集的结果，再将训练集数据的坐标在结果集的坐标中分别比较，找到最近的坐标，判断分类是都正确，得到正确率

### 关键代码
knn
```
def classify(inX, dataSet, labels, k):
    inX = np.mat(inX)
    dataSet = np.mat(dataSet)
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = np.array(diffMat) **2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for j in labels[0]:
        classCount[j] = 0
    labels = np.mat(labels)
    for i in range(k):
        voteIlabel = labels[0, sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
```
测试
```
def check():
    print("loadTrainData()")
    trainData, trainLabel = loadTrainData()
    print("loadResultData()")
    resultData, resultLabel = loadResultData()
    m, n = np.shape(trainData)
    errorCount = 0
    print("checking...")
    for i in range(m):
        print("rate of progress: %.2f%%" % (i/m * 100))
        labelindex = -1
        x = (trainData[i, 0] + 10)//20*20
        y = (trainData[i, 1] + 10)//20*20
        for index in range(1000000):
            if resultData[index, 0] == x and resultData[index, 1] == y:
                labelindex = index
                break
        if trainLabel[i] != resultLabel[labelindex]:
            errorCount += 1.0
    print ("\nthe total number of errors is: %d" % errorCount)
    print ("\nthe total accuracy is: %f" % (1 - errorCount/float(m)))

```

### 实验结果
![实验结果][2]
![实验结果2][3]

the total number of errors is: 1
the total accuracy is: 0.998069

  [1]: https://img1.doubanio.com/view/status/m/public/a34af2a4fa6178b.webp
  [2]: https://img3.doubanio.com/view/status/m/public/2fed8cc1ad11190.webp
  [3]: https://img3.doubanio.com/view/status/m/public/1882f5a770fcf0d.webp