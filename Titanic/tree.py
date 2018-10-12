# -*- coding: utf-8 -*-
from sklearn.preprocessing import Imputer
from sklearn import tree
import operator
import numpy as np
import csv
import pdb

def loadTrainData():
    l = []
    with open('refineTrain.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l = np.array(l[1:])
    label = l[:, 2]
    data = l[:, 2:]
    return toArr(data), label

def loadTestData():
    l = []
    with open('refineTest.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l = np.array(l[1:])
    data = l[:, 1:]
    return toArr(data)

def toArr(arr):
    n,m = arr.shape
    arr = np.array(arr, dtype=float)
    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
    imp.fit(arr)
    res_arr = imp.transform(arr)
    return res_arr

def classify(testDataSet, testLabels, dataSet, labels):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(dataSet, labels)
    n,m = testDataSet.shape
    errorCount = 0
    predictedLabel = clf.predict_proba(testDataSet[:])
    print(predictedLabel)
    return

def Test():
    print("loadTrainData()")
    trainData, trainLabel = loadTrainData()
    print("loadTestData()")
    testData = loadTestData()
    classify(testData, [], trainData, trainLabel)

if __name__ == "__main__":
    Test()