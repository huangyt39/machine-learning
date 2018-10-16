# -*- coding: utf-8 -*-
import xlrd
import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def read_excel():
    workbook = xlrd.open_workbook(r'./Export_Output.xlsx')
    sheet = workbook.sheet_by_index(0)
    row_num, col_num = sheet.nrows, sheet.ncols

    # A, B, C = [], [], []
    # for i in range(row_num):
    #     # print("row", i, sheet.row_values(i))
    #     if sheet.row_values(i)[0] == 'A':
    #         A.append([sheet.row_values(i)[1], sheet.row_values(i)[2]])
    #     elif sheet.row_values(i)[0] == 'B':
    #         B.append([sheet.row_values(i)[1], sheet.row_values(i)[2]])
    #     elif sheet.row_values(i)[0] == 'C':
    #         C.append([sheet.row_values(i)[1], sheet.row_values(i)[2]])
    # print(A, B, C)
    data = []
    for i in range(1, row_num):
        str_tmp = []
        str_tmp.append(str(sheet.row_values(i)[5]))
        str_tmp.append(str(sheet.row_values(i)[7]))
        str_tmp.append(str(sheet.row_values(i)[6]))
        data.append(str_tmp)
    print(data)
    saveData(data)
    # return A, B, C

def showMaxmin():
    l,lon,lat = [],[],[]
    with open('export_output.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    for index in l:
        lon.append(float(index[1]))
        lat.append(float(index[2]))
    lonarr, latarr = np.array(lon), np.array(lat)
    print(np.min(lonarr), np.max(lonarr))
    print(np.min(latarr), np.max(latarr))
    

def showInScatter(A, B, C):
    plt.scatter([nums[0] for nums in A], [nums[1] for nums in A], c = 'g', s = 5)
    plt.scatter([nums[0] for nums in B], [nums[1] for nums in B], c = 'r', s = 5)
    plt.scatter([nums[0] for nums in C], [nums[1] for nums in C], c = 'b', s = 5)
    plt.show()

def saveData(data):
    with open('export_output.csv', 'w', newline="") as myFile:
        myWriter = csv.writer(myFile)
        for str_line in data:
            tmp = []
            tmp.append(str_line)
            # print("tmp: ", tmp)
            # print("str_line: ", str_line)
            myWriter.writerow(str_line)

def showData():
    l = []
    with open('drill.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    A, B, C = [], [], []
    for index in l[1:]:
        if index[2] == 'B':
            B.append([int(float(index[0])), int(float(index[1]))])
        if index[2] == 'C':
            C.append([int(float(index[0])), int(float(index[1]))])
        if index[2] == 'A':
            A.append([int(float(index[0])), int(float(index[1]))])

    plt.scatter([nums[0] for nums in A], [nums[1] for nums in A], c = 'g', s = 10)
    plt.scatter([nums[0] for nums in B], [nums[1] for nums in B], c = 'r', s = 10)
    plt.scatter([nums[0] for nums in C], [nums[1] for nums in C], c = 'b', s = 10)
    plt.show()

def showResult():
    l = []
    with open('result.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    A, B, C = [], [], []
    for index in l[:]:
        if index[2] == 'B':
            B.append([int(float(index[0])), int(float(index[1]))])
        if index[2] == 'C':
            C.append([int(float(index[0])), int(float(index[1]))])
        if index[2] == 'A':
            A.append([int(float(index[0])), int(float(index[1]))])
    plt.scatter([nums[0] for nums in A], [nums[1] for nums in A], c = 'g', s = 1, marker=',')
    plt.scatter([nums[0] for nums in B], [nums[1] for nums in B], c = 'r', s = 1, marker=',')
    plt.scatter([nums[0] for nums in C], [nums[1] for nums in C], c = 'b', s = 1, marker=',')
    plt.show()
    
#生成测试坐标数据
def createData():
    data = []
    for i in range(1000):
        for j in range(1000):
            data.append([412000 + j*40, 2541000 + i*40])
    with open('test.csv', 'w', newline="") as myFile:
        myWriter = csv.writer(myFile)
        for str_line in data:
            tmp = []
            tmp.append(str_line)
            # print("tmp: ", tmp)
            # print("str_line: ", str_line)
            myWriter.writerow(str_line)

def showResultData():
    l = []
    with open('result.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    A, B, C = [], [], []
    for index in l[:]:
        if index[2] == 'B':
            B.append([int(float(index[0])), int(float(index[1]))])
        if index[2] == 'C':
            C.append([int(float(index[0])), int(float(index[1]))])
        if index[2] == 'A':
            A.append([int(float(index[0])), int(float(index[1]))])
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
        if index[2] == 'B':
            B.append([int(float(index[0])), int(float(index[1]))])
        if index[2] == 'C':
            C.append([int(float(index[0])), int(float(index[1]))])
        if index[2] == 'A':
            A.append([int(float(index[0])), int(float(index[1]))])

    plt.scatter([nums[0] for nums in A], [nums[1] for nums in A], c = 'k', s = 2, marker='o')
    plt.scatter([nums[0] for nums in B], [nums[1] for nums in B], c = 'k', s = 2, marker='o')
    plt.scatter([nums[0] for nums in C], [nums[1] for nums in C], c = 'k', s = 2, marker='o')

    l1 = plt.scatter([nums[0] for nums in A], [nums[1] for nums in A], c = 'g', s = 1, marker='o')
    l2 = plt.scatter([nums[0] for nums in B], [nums[1] for nums in B], c = 'r', s = 1, marker='o')
    l3 = plt.scatter([nums[0] for nums in C], [nums[1] for nums in C], c = 'b', s = 1, marker='o')
 
    chinese =matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf')
    plt.legend(handles =[l2,l3] , labels=['中软土','中硬土'], loc = 'best', prop=chinese)

    plt.show()

def showWorkArea():
    l = []
    with open('export_output.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    data = []
    for index in l[:]:
        data.append([float(index[1]), float(index[2])])

    plt.scatter([nums[0] for nums in data], [nums[1] for nums in data], c = 'k', s = 1, marker='o')
    plt.show()

#x = (412884,450819) 37935 => 412000~452000 40000
#y = (2546524, 2575622) 29098 => 2541000~2581000 40000

def showResultWorkArea():
    l = []
    with open('tranresult.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    A, B, C = [], [], []
    for index in l[:]:
        if index[2] == 'B':
            B.append([float(index[0]), float(index[1])])
        if index[2] == 'C':
            C.append([float(index[0]), float(index[1])])
        if index[2] == 'A':
            A.append([float(index[0]), float(index[1])])
    l1 = plt.scatter([nums[0] for nums in A], [nums[1] for nums in A], c = 'darkolivegreen', s = 1, marker=',')
    l2 = plt.scatter([nums[0] for nums in B], [nums[1] for nums in B], c = 'indianred', s = 1, marker=',')
    l3 = plt.scatter([nums[0] for nums in C], [nums[1] for nums in C], c = 'royalblue', s = 1, marker=',')
 
    l = []
    with open('export_output.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    data = []
    for index in l[:]:
        data.append([float(index[1]), float(index[2])])
    l1 = plt.scatter([nums[1] for nums in data], [nums[0] for nums in data], c = 'k', s = 1, marker=',')

    chinese =matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf')
    plt.legend(handles =[l2,l3] , labels=['中软土','中硬土'], loc = 'best', prop=chinese)

    plt.show()