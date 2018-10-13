# -*- coding: utf-8 -*-
from sklearn.preprocessing import Imputer
from sklearn import tree
import operator
import numpy as np
import csv
import pdb
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def loadTrainData():
    l = []
    with open('refineTrain.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l = np.array(l[1:])
    label = l[:, 1]
    data = l[:, 3:]
    return toArr(data), label

def loadTestData():
    l = []
    with open('refineTest.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l = np.array(l[1:])
    data = l[:, 2:]
    return toArr(data)

def loadTestId():
    l = []
    with open('refineTest.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l = np.array(l[1:])
    data = l[:, 0]
    return data

def toArr(arr):
    n,m = arr.shape
    arr = np.array(arr, dtype=float)
    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
    imp.fit(arr)
    res_arr = imp.transform(arr)
    return res_arr

def classify(testDataSet, testLabels, dataSet, labels):
    clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3,min_samples_leaf=5)
    clf = clf.fit(dataSet, labels)
    n,m = testDataSet.shape
    errorCount = 0
    predictedLabel = clf.predict(testDataSet[:])
    print(predictedLabel)

    # for i in range(n):
    #     if predictedLabel[i] != labels[i]:
    #         errorCount += 1
    
    # print("the total accuracy is: {:.2f}".format(clf.score(testDataSet,testLabels)))
    
    # 查看特征的重要程度
    # feature_importance = clf.feature_importances_
    # important_features = [x for x in range(2, 8)]
    # feature_importance = 100.0 * (feature_importance / feature_importance.max())
    # sorted_idx = np.argsort(feature_importance)[::-1]
    # pos = np.arange(sorted_idx.shape[0]) + .5

    # plt.title('Feature Importance')
    # plt.barh(pos, feature_importance[sorted_idx[::-1]], color='r',align='center')
    # plt.yticks(pos, important_features)
    # plt.xlabel('Relative Importance')
    # plt.draw()
    # plt.show()
    return predictedLabel

def Test():
    print("loadTrainData()")
    trainData, trainLabel = loadTrainData()
    print("loadTestData()")
    testData = loadTestData()
    # X_train, X_test, y_train, y_test = train_test_split(trainData, trainLabel, test_size=0.25, random_state=33)
    # classify(X_test, y_test, X_train, y_train)
    result = classify(testData, [], trainData, trainLabel)
    saveResult(result)

def saveResult(data):
    testId = loadTestId()
    n = data.shape[0]
    with open('result.csv', 'w', newline="") as myFile:
        myWriter = csv.writer(myFile)
        for index in range(n):
            str_line = int(float(data[index]))
            tmp = []
            tmp.append(int(float(testId[index])))
            tmp.append(str_line)
            myWriter.writerow(tmp)

if __name__ == "__main__":
    Test()