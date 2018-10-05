# -*- coding: utf-8 -*-
import csv

l = []
with open('result.csv') as myfile:
    lines = csv.reader(myfile)
    for line in lines:
        if line != []:
            line[1] = line[1][:-2]
            l.append(line)
    
with open('resultt.csv', 'w', newline='') as myFile:
    myWriter = csv.writer(myFile)
    myWriter.writerow(['ImageId', 'Label'])
    for str_line in l:
        myWriter.writerow(str_line)