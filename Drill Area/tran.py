import csv
from math import *

def tran(x, yy):
    y = yy
    L0 = 0
    p=206264.80625
    i = 1
    while yy/i >= 10:
        y = yy - (int)(yy / i) * i-500000
        L0 =117
        i *= 10  
    bt = x / 6367558.4969*p
    BT = x / 6367558.4969
    c3=cos(BT)*cos(BT)
    c4=sin(BT)*cos(BT)
    Bf=(bt+(50221746+(293622+(2350+22*c3)*c3)*c3)*c4*(10**-10)*p)/p
    c5=cos(Bf)**2
    c6=sin(Bf)*cos(Bf)
    Nf=6399698.902-(21562.267-(108.973-0.612*c5)*c5)*c5
    Z=y/(Nf*cos(Bf))
    b2 = (0.5 + 0.003369 * c5) * c6
    b3 = 0.333333 - (0.166667 - 0.001123 * c5) * c5
    b4 = 0.25 + (0.16161 + 0.00562 * c5) * c5
    b5=0.2-(0.1667-0.0088*c5)*c5
    z2=Z**2
    B = (Bf*p - (1 - (b4 - 0.12 *z2) * z2) * z2 * b2 * p)/3600.0
    L = L0+((1 - (b3 - b5 * z2) * z2) * Z * p)/3600.0
    return L, B

def tranData():
    l, data = [], []
    with open('result.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
        for index in l[:]:
            tmp = list(tran(float(index[1]), float(index[0])))
            tmp.append(index[2])
            data.append(tmp)

    with open('tranresult.csv', 'w', newline="") as myFile:
        myWriter = csv.writer(myFile)
        for str_line in data:
            tmp = []
            tmp.append(str_line)
            myWriter.writerow(str_line)

if __name__ == "__main__":
    tranData()