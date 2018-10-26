# -*- coding: utf-8 -*-
import csv
from numpy import *
import numpy as np
import operator
import matplotlib.pyplot as plt
import matplotlib
import shapefile
from sklearn.svm import SVC
import pdb

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

def saveResult(result):
    with open('result.csv', 'w', newline="") as myFile:
        myWriter = csv.writer(myFile)
        for str_line in result:
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
    # svc=SVC(kernel='poly',degree=2,gamma=1,coef0=0)
    svc=SVC(C=10, kernel='rbf', degree=1, gamma=20, coef0=0.0)
    svc.fit(trainData, trainLabel)
    resultList = svc.predict(testData)
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

def loadTestData():
    l = []
    with open('test.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l = np.array(l)
    data = l[:,]
    return toFloat(data)

def loadResultLabel():
    l = []
    with open('result.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    label = []
    for sublabel in l:
        tmp = sublabel[0] + sublabel[1] + sublabel[2]
        label.append(tmp)
    label = np.array(label)
    return label

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
        x = (trainData[i, 0] + 0.00042291188458473526//2)//0.00042291188458473526*0.00042291188458473526
        y = (trainData[i, 1] + 0.0003447908845059189//2)//0.0003447908845059189*0.0003447908845059189
        for index in range(17052):
            if abs(resultData[index, 0] - x) <= 0.05 and abs(resultData[index, 1] - y) <= 0.04:
                labelindex = index
                break
        print(labelindex, trainLabel[i], resultLabel[labelindex])
        if trainLabel[i] != resultLabel[labelindex]:
            errorCount += 1.0
    print ("\nthe total number of errors is: %d" % errorCount)
    print ("\nthe total accuracy is: %f" % (1 - errorCount/float(m)))

if __name__ == '__main__':
    DrillTest()
