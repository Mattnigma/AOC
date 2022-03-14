#! /usr/bin/env python3

x=0
y=0
aim=0
newstring=[]
data=open("./data_02-1.txt")
templist=data.readlines()
for line in templist:
    line=line.replace("forward","")
    line=line.replace("up","1")
    line=line.replace("down","2")
    line=line.replace(" ","")
    line=line.replace("\n","")
    line=int(line)
    newstring.append(line)

for num in newstring:
    if num<10:
        x=x+num
        y=aim*num+y
    elif num<20:
        num=num-10
        aim=aim-num
    else:
        num=num-20
        aim=aim+num

sum=x*y
print(sum)