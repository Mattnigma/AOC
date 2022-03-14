#! /usr/bin/env python3

depth1=1000
increases=0
data=open("./1-1data.txt")
slist=data.readlines()
list=[int(y) for y in slist]
x=1000
y=1000
z=1000


for depth in list:
    if depth>x:
        increases+=1
    x=y
    y=z
    z=depth

print(increases)