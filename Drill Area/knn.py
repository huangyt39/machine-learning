# -*- coding: utf-8 -*-
import csv
import rdData
from numpy import *
import numpy as np
import operator

def loadTrainData():
    l = []
    with open('drill.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l = np.array(l)
    label = l[:, -1]
    data = l[:, :-1]
    return toInt(data), label

def toInt(array):
    array = np.mat(array)
    m, n = np.shape(array)
    res = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            res[i, j] = int(float(array[i, j]))
    return res

def normalizing(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet/tile(ranges, (m, 1))
    return normDataSet

def loadTestData():
    l = []
    with open('test.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l = np.array(l)
    return toInt(l), normalizing(toInt(l))

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

def saveResult(result):
    with open('result.csv', 'w', newline="") as myFile:
        myWriter = csv.writer(myFile)
        for str_line in result:
            tmp = []
            tmp.append(str_line)
            # print("tmp: ", tmp)
            # print("str_line: ", str_line)
            myWriter.writerow(str_line)

def DrillTest():
    print("loadTrainData()")
    trainData, trainLabel = loadTrainData()
    trainData = normalizing(trainData)
    print("loadTestData()")
    testData, norTestData = loadTestData()
    m,n = np.shape(testData)
    errorCount=0
    resultList=[]
    print("classify()")
    for i in range(m):
        classifierResult = classify(norTestData[i], trainData, trainLabel, 1)
        resultList.append([str(testData[i][0]), str(testData[i][1]), str(classifierResult)])
        print ("the classifier came back with: %s, rate of progress: %.2f%%" % (classifierResult, i/m * 100))
    saveResult(resultList)

if __name__ == '__main__':
    # rdData.read_excel()
    # rdData.showData()
    # rdData.createData()
    DrillTest()
    check()
    rdData.showResult()

def loadResultData():
    l = []
    with open('result.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l = np.array(l)
    label = l[:, -1]
    data = l[:, :-1]
    return normalizing(toInt(data)), label

def check():
    print("loadTrainData()")
    trainData, trainLabel = loadTrainData()
    print("loadResultData()")
    resultData, resultLabel = loadResultData()
    m, n = np.shape(trainData)
    errorCount = 0
    print("checking...")
    for i in range(m):
        labelindex = -1
        x = (trainData[i, 0]//10)*10
        y = (trainData[i, 1]//10)*10
        for index in range(16000):
            if resultData[index, 0] == x and resultData[index, 1] == y:
                labelindex = index
                # print(resultData[index, 0], x, resultData[index, 1], y)
                break
        if trainLabel[i] != resultLabel[labelindex]:
            errorCount += 1.0
    print ("\nthe total number of errors is: %d" % errorCount)
    print ("\nthe total error rate is: %f" % (errorCount/float(m)))

# the total number of errors is: 206
# the total error rate is: 0.397683