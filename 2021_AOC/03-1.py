#! /usr/bin/env python3

# Read puzzle input from file into 2D char array
data=open("./data_03-1.txt")
templist=data.readlines()
newstring=[]
for string in templist:
    subarray=list(string)
    newstring.append(subarray)

# count '1's in each column
c1=0
complist=[]
for substring in newstring[0]:
    c2=0
    x=0
    for sublist in newstring:
        y=newstring[c2][c1]
        if y=="\n":
            break
        ny=int(y)
        x=ny+x
        c2+=1
    if x!=0:
        complist.append(x)
    c1+=1

half=int(len(templist)/2)
gamma=""
epsilon=""
for num in complist:
    if num>half:
        x=1
        y=0
    else:
        x=0
        y=1
    gamma+=str(x)
    epsilon+=str(y)

intgamma=int(gamma,2)
intepsilon=int(epsilon,2)

print(intgamma*intepsilon)