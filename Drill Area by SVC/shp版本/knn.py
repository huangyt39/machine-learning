# -*- coding: utf-8 -*-
import csv
from numpy import *
import numpy as np
import operator
import matplotlib.pyplot as plt
import matplotlib
import shapefile
from matplotlib.path import Path
from matplotlib.patches import PathPatch

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
    fig = plt.figure()
    ax = fig.add_subplot(111)

    shape_rec = sf.shapeRecords()[-1]
    vertices = []
    codes = []
    pts = shape_rec.shape.points
    prt = list(shape_rec.shape.parts) + [len(pts)]
    for i in range(len(prt) - 1):
        for j in range(prt[i], prt[i+1]):
            vertices.append((pts[j][0], pts[j][1]))
        codes += [Path.MOVETO]
        codes += [Path.LINETO] * (prt[i+1] - prt[i] -2)
        codes += [Path.CLOSEPOLY]
    clip = Path(vertices, codes)
    clip = PathPatch(clip, transform=ax.transData, edgecolor='k')

    # xx, yy = np.meshgrid(np.linspace(xx_min, xx_max, 1000), np.linspace(yy_min, yy_max, 1000), copy=False)
    xx, yy = np.meshgrid(xtmp, ytmp, copy=False)
    zz = []
    for i in range(len(xx)):
        tmp = []
        for j in range(len(yy)):
            tmp.append(point2color[str(xx[i][j])[:8] + "+" +str(yy[i][j])[0:7]])
        zz.append(tmp)

    cont = plt.contourf(xx, yy, zz, 1)
    #brg plt.cm.hot
    
    for col in cont.collections:
        col.set_clip_path(clip)
    
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

#     plt.scatter([nums[0] for nums in A], [nums[1] for nums in A], c = 'k', s = 2, marker='o')
    plt.scatter([nums[0] for nums in B], [nums[1] for nums in B], c = 'k', s = 2, marker='o')
    plt.scatter([nums[0] for nums in C], [nums[1] for nums in C], c = 'k', s = 2, marker='o')

#     l1 = plt.scatter([nums[0] for nums in A], [nums[1] for nums in A], c = 'r', s = 1, marker='o')
    l2 = plt.scatter([nums[0] for nums in B], [nums[1] for nums in B], c = 'cornflowerblue', s = 2, marker='o')
    l3 = plt.scatter([nums[0] for nums in C], [nums[1] for nums in C], c = 'lime', s = 2, marker='o')
 
    chinese =matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf')
    plt.legend(handles =[l2,l3] , labels=['中软土','中硬土'], loc = 'best', prop=chinese)

#     sf = shapefile.Reader('./范围/范围.shp')
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        plt.plot(x,y,c='k')
    figure_fig = plt.gcf()  # 'get current figure'
    figure_fig.savefig('./result/result.eps', format='eps', dpi=1000)
    figure_fig.savefig('./result/result.jpg', format='jpg', dpi=1000)
    plt.show()

if __name__ == '__main__':
    DrillTest()
    # showResultData()
