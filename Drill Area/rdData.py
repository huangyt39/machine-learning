# -*- coding: utf-8 -*-
import xlrd
import csv
import numpy as np
import matplotlib.pyplot as plt

def read_excel():
    workbook = xlrd.open_workbook(r'./drill.xlsx')
    sheet = workbook.sheet_by_index(0)
    row_num, col_num = sheet.nrows, sheet.ncols

    A, B, C = [], [], []
    for i in range(row_num):
        # print("row", i, sheet.row_values(i))
        if sheet.row_values(i)[0] == 'A':
            A.append([sheet.row_values(i)[1], sheet.row_values(i)[2]])
        elif sheet.row_values(i)[0] == 'B':
            B.append([sheet.row_values(i)[1], sheet.row_values(i)[2]])
        elif sheet.row_values(i)[0] == 'C':
            C.append([sheet.row_values(i)[1], sheet.row_values(i)[2]])
    # print(A, B, C)
    data = []
    for i in range(1, row_num):
        str_tmp = []
        str_tmp.append(str(sheet.row_values(i)[1]))
        str_tmp.append(str(sheet.row_values(i)[2]))
        str_tmp.append(str(sheet.row_values(i)[0]))
        data.append(str_tmp)
    print(data)
    saveData(data)
    return A, B, C

def showInScatter(A, B, C):
    plt.scatter([nums[0] for nums in A], [nums[1] for nums in A], c = 'g', s = 5)
    plt.scatter([nums[0] for nums in B], [nums[1] for nums in B], c = 'r', s = 5)
    plt.scatter([nums[0] for nums in C], [nums[1] for nums in C], c = 'b', s = 5)
    plt.show()

def saveData(data):
    with open('drill.csv', 'w', newline="") as myFile:
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
    for i in range(400):
        for j in range(400):
            data.append([412000 + 0.5 + j*10, 2541000 + 0.5 + i*10])
    with open('test.csv', 'w', newline="") as myFile:
        myWriter = csv.writer(myFile)
        for str_line in data:
            tmp = []
            tmp.append(str_line)
            # print("tmp: ", tmp)
            # print("str_line: ", str_line)
            myWriter.writerow(str_line)

#x = (412884,450819) 37935 => 412000~452000 40000
#y = (2546524, 2575622) 29098 => 2541000~2581000 40000