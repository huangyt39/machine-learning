# -*- coding: utf-8 -*-
import csv
from numpy import *
import numpy as np
import operator
import matplotlib.pyplot as plt
import matplotlib
import shapefile

def loadTrainData():
    l = []
    with open('drill.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l = np.array(l)
    label = l[:, -1]
    data = l[:, :-1]
    return toFloat(data), label

def toFloat(array):
    array = np.mat(array)
    m, n = np.shape(array)
    res = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            res[i, j] = float(array[i, j])
    return res

def loadTestData():
    l = []
    with open('test.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l = np.array(l)
    return toFloat(l)

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
            myWriter.writerow(str_line)

def DrillTest():
    print("loadTrainData()")
    trainData, trainLabel = loadTrainData()
    print("loadTestData()")
    testData = loadTestData()
    m,n = np.shape(testData)
    errorCount=0
    resultList=[]
    print("classify()")
    for i in range(m):
        classifierResult = classify(testData[i], trainData, trainLabel, 9)
        resultList.append([str(testData[i][0]), str(testData[i][1]), str(classifierResult)])
        print ("the classifier came back with: %s, rate of progress: %.2f%%" % (classifierResult, i/m * 100))
    saveResult(resultList)

def loadResultData():
    l = []
    with open('result.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l = np.array(l)
    label = l[:, -1]
    data = l[:, :-1]
    return toFloat(data), label

def check():
    print("loadTrainData()")
    trainData, trainLabel = loadTrainData()
    print("loadResultData()")
    resultData, resultLabel = loadResultData()
    m, n = np.shape(trainData)
    errorCount = 0
    print("checking...")
    for i in range(m):
        print("checking...rate of progress: %.2f%%" % (i/m * 100))
        labelindex = -1
        x = (trainData[i, 0] + 0.00225)//0.0045*0.0045
        y = (trainData[i, 1] + 0.00015)//0.0003*0.0003
        for index in range(1000000):
            if resultData[index, 0] == x and resultData[index, 1] == y:
                labelindex = index
                break
        if trainLabel[i] != resultLabel[labelindex]:
            errorCount += 1.0
    print ("\nthe total number of errors is: %d" % errorCount)
    print ("\nthe total accuracy is: %f" % (1 - errorCount/float(m)))

def showResultData():
    l = []
    with open('result.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    A, B, C = [], [], []
    for index in l[:]:
        if int(float(index[2])) == 1:
            B.append([float(index[0]), float(index[1])])
        if int(float(index[2])) == 2:
            C.append([float(index[0]), float(index[1])])
        if int(float(index[2])) == 0:
            A.append([float(index[0]), float(index[1])])
    plt.scatter([nums[0] for nums in A], [nums[1] for nums in A], c = 'darkolivegreen', s = 1, marker=',')
    plt.scatter([nums[0] for nums in B], [nums[1] for nums in B], c = 'indianred', s = 1, marker=',')
    plt.scatter([nums[0] for nums in C], [nums[1] for nums in C], c = 'royalblue', s = 1, marker=',')
    
    l = []
    with open('drill.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    A, B, C = [], [], []
    for index in l[1:]:
        if int(float(index[2])) == 1:
            B.append([float(index[0]), float(index[1])])
        if int(float(index[2])) == 2:
            C.append([float(index[0]), float(index[1])])
        if int(float(index[2])) == 0:
            A.append([float(index[0]), float(index[1])])

    plt.scatter([nums[0] for nums in A], [nums[1] for nums in A], c = 'k', s = 2, marker='o')
    plt.scatter([nums[0] for nums in B], [nums[1] for nums in B], c = 'k', s = 2, marker='o')
    plt.scatter([nums[0] for nums in C], [nums[1] for nums in C], c = 'k', s = 2, marker='o')

    l1 = plt.scatter([nums[0] for nums in A], [nums[1] for nums in A], c = 'g', s = 1, marker='o')
    l2 = plt.scatter([nums[0] for nums in B], [nums[1] for nums in B], c = 'r', s = 1, marker='o')
    l3 = plt.scatter([nums[0] for nums in C], [nums[1] for nums in C], c = 'b', s = 1, marker='o')
 
    chinese =matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf')
    plt.legend(handles =[l2,l3] , labels=['中软土','中硬土'], loc = 'best', prop=chinese)

    sf = shapefile.Reader('范围.shp')
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        plt.plot(x,y)

    plt.show()

if __name__ == '__main__':
    DrillTest()
    showResultData()
