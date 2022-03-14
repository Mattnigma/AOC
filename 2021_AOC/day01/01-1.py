#! /usr/bin/env python3

depth1=1000
increases=0

for depth in open("./1-1data.txt").readlines():
    depth=int(depth)
    if depth > depth1:
        increases+=1
    depth1=depth

print(increases)