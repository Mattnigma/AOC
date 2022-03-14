#! /usr/bin/env python3

def open_file_and_parse(test_or_main):
    #open correct file
    if test_or_main=="test":
        data=open("./data_09_test.txt")
    elif test_or_main=="temp":
        data=open("./temp.txt")
    else:
        data=open("./data_09.txt")
    data=data.readlines()
    matrix=[]
    for row in data:
        matrix.append([int(x) for x in row.strip()])
    return matrix

def map_basin(starting_point,map):
    this_basin=[]
    this_basin.append(starting_point)
    i=0
    while i==0:
        new_points=[]
        for point in this_basin:
            if point[0]!=0:
                if map[point[0]-1][point[1]]!=9:
                    new_points.append([point[0]-1,point[1]])
            if point[0]!=len(map)-1:
                if map[point[0]+1][point[1]]!=9:
                    new_points.append([point[0]+1,point[1]])
            if point[1]!=0:
                if map[point[0]][point[1]-1]!=9:
                    new_points.append([point[0],point[1]-1])
            if point[1]!=len(map[0])-1:
                if map[point[0]][point[1]+1]!=9:
                    new_points.append([point[0],point[1]+1])
        old_basin_size=len(this_basin)
        for point in new_points:
            if point not in this_basin:
                this_basin.append(point)
        new_basin_size=len(this_basin)
        if new_basin_size==old_basin_size:
            i=1
    basin_size=len(this_basin)
    return this_basin , basin_size

def find_low_points(map):
    low_points=[]
    i=0
    while i < len(map):
        j=0
        while j < len(map[0]):
            x=0
            if i!=0:
                if map[i][j]>=map[i-1][j]:
                    x=1
            if i!=len(map)-1:
                if map[i][j]>=map[i+1][j]:
                    x=1
            if j!=0:
                if map[i][j]>=map[i][j-1]:
                    x=1
            if j!=len(map[0])-1:
                if map[i][j]>=map[i][j+1]:
                    x=1
            if x==0:
                low_points.append([i,j])
            j+=1
        i+=1
    return low_points

def find_3_highest(basin_sizes):
    largest_3=[0,0,0]
    for size in basin_sizes:
        if size>largest_3[0]:
            largest_3[0]=size
            largest_3=sorted(largest_3)
    return largest_3


def main(type):
    hight_map=open_file_and_parse(type)
    low_points=find_low_points(hight_map)
    all_basin_points=[]
    basin_sizes=[]
    for point in low_points:
        if point not in all_basin_points:
            basin_points , basin_len = map_basin(point, hight_map)
            for sub_point in basin_points:
                all_basin_points.append(sub_point)
            basin_sizes.append(basin_len)
    largest_3=find_3_highest(basin_sizes)
    answer=largest_3[0]*largest_3[1]*largest_3[2]
    print(answer)
    


type="main"
# doc_type="temp"
# doc_type="test"



main(type)