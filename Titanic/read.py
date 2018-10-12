# -*- coding: utf-8 -*-
import xlrd
import csv
import numpy as np

def read_excel():
    workbook = xlrd.open_workbook(r'./test-csv.xlsx')
    sheet = workbook.sheet_by_index(0)
    row_num, col_num = sheet.nrows, sheet.ncols

    data = []
    for i in range(row_num):
        str_tmp = []
        for j in range(col_num):
            str_tmp.append(sheet.row_values(i)[j])
        data.append(str_tmp)
    
    with open('refineTest.csv', 'w', newline="") as myfile:
        myWriter = csv.writer(myfile)
        for str_line in data:
            tmp = []
            tmp.append(str_line)
            myWriter.writerow(str_line)
    
if __name__ == "__main__":
    read_excel()