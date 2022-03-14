#! /usr/bin/env python3

from copy import copy

# Read puzzle input from file into 2D char array
data=open("./data_03-1.txt")
templist=data.readlines()

i=0

while i<len(templist):
    templist[i]=list(templist[i])
    j=0
    templist[i].remove("\n")
    while j<len(templist[i]):
        if templist[i][j]=="\n":
            templist=templist[i][j].replace("\n","")
        else:
            templist[i][j]=int(templist[i][j])
        j+=1
    i+=1


def trimfat(array2d,j,pos):
    i=0
    x=0
    while i<len(array2d):
        x+=array2d[i][j]
        i+=1
    if x>=len(array2d)/2:
        if pos==1:
            y=1
        else:
            y=0
    else:
        if pos==1:
            y=0
        else:
            y=1
    i=0
    k=0
    dc=0
    while k<len(array2d):
        if array2d[k][j]!=y:
            array2d.remove(array2d[k])
            dc+=1
        else:
            k+=1
    return array2d

o2=copy(templist)
co2=copy(templist)

i=0
for it in templist[0]:
    if len(o2)==1:
        break
    else:
        o2=trimfat(o2,i,1)
    i+=1

i=0
for it in templist[0]:
    if len(co2)==1:
        break
    else:
        co2=trimfat(co2,i,0)
    i+=1

stro2=""
strco2=""
i=0
for gas in o2[0]:
    stro2+=str(o2[0][i])
    i+=1
i=0
for gas in co2[0]:
    strco2+=str(co2[0][i])
    i+=1

intco2=int(strco2,2)
into2=int(stro2,2)

print(into2*intco2)