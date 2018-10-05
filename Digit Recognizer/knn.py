# -*- coding: utf-8 -*-
import csv

import numpy as np
import operator


def loadTrainData():
    l = []
    with open('train.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l.remove(l[0])
    l = np.array(l)
    label = l[:, 0]
    data = l[:, 1:]
    return normalizing(toInt(data)), toInt(label)

def toInt(array):
    array = np.mat(array)
    m, n = np.shape(array)
    res = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            res[i, j] = int(array[i, j])
    return res

def normalizing(array):
    m, n = np.shape(array)
    for i in range(m):
        for j in range(n):
            if array[i, j] > 0:
                array[i, j] = 1
    return array

def loadTestData():
    l = []
    with open('test.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l.remove(l[0])
    l = np.array(l)
    return normalizing(toInt(l))

# def loadTestResult():
#     l = []
#     with open('sample_submission.csv') as file:
#         lines = csv.reader(file)
#         for line in lines:
#             l.append(line)
#     l.remove(l[0])
#     res = np.array(l)
#     return toInt(res[:, 1])

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
    with open('result.csv', 'w') as myFile:
        myWriter = csv.writer(myFile)
        for str_line in result:
            tmp = []
            tmp.append(str_line)
            # print("tmp: ", tmp)
            # print("str_line: ", str_line)
            myWriter.writerow(str_line)

def handwritingClassTest():
    print("loadTrainData()")
    trainData, trainLabel = loadTrainData()
    print("loadTestData()")
    testData = loadTestData()
    # print("loadTestResult()")
    # testLabel = loadTestResult()
    m,n = np.shape(testData)
    errorCount=0
    resultList=[]
    print("classify()")
    for i in range(m):
        classifierResult = classify(testData[i], trainData, trainLabel, 5)
        resultList.append([str(i + 1), str(classifierResult)])
        print ("the classifier came back with: %d, rate of progress: %.2f%%" % (classifierResult, i/m * 100))
    #     if (classifierResult != testLabel[0,i]): errorCount += 1.0
    # print ("\nthe total number of errors is: %d" % errorCount)
    # print ("\nthe total error rate is: %f" % (errorCount/float(m)))
    saveResult(resultList)

if __name__ == '__main__':
    handwritingClassTest()
