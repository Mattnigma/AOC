#! /usr/bin/env python3


def open_file_and_parse(test_or_main):
    #open correct file
    if test_or_main=="test":
        data=open("./data_05_test.txt")
        data=data.readlines()
    else:
        data=open("./data_05.txt")
        data=data.readlines()
    i=0
    #parse into 2d array
    while i < len(data):
        data[i]=data[i].replace(","," ").replace("\n","").replace("->","")
        data[i]=data[i].split()
        data[i]=[int(number) for number in data[i]]
        i+=1
    i=0
    #parse into 3d array with innermost lists containing sets of x or y coordinates
    while i <len(data):
        data[i]=[[ data[i][0] , data[i][2] ],[ data[i][1], data[i][3] ]]
        i+=1
    return data

def generate_blank_map(test_or_main):
    if test_or_main=="test":
        x=9
    else:
        x=999
    i=0
    map=[]
    while i<=x:
        j=0
        map.append([])
        while j<=x:
            map[i].append(0)
            j+=1
        i+=1
    return map

def convert_vectors_to_points(vector_list):
    points_list=[]
    for vector in vector_list:
        j=0
        if vector[0][0]==vector[0][1]:
            while j <= abs(vector[1][0]-vector[1][1]):
                points_list.append([vector[0][0],min(vector[1][0],vector[1][1])+j])
                j+=1
        elif vector[1][0]==vector[1][1]:
            while j <= abs(vector[0][0]-vector[0][1]):
                points_list.append([min(vector[0][0],vector[0][1])+j,vector[1][0]])
                j+=1
    return points_list

def mark_points_on_map(point_list, input_map):
    map=input_map.copy()
    for point in point_list:
        map[point[0]][point[1]]+=1
    return map

def calculate_points_w_intersecting_lines(map):
    points=0
    for row in map:
        for column in row:
            if column>1:
                points+=1
    return points


def main(type):
    vent_locations=open_file_and_parse(type)
    map=generate_blank_map (type)
    points_list=convert_vectors_to_points(vent_locations)
    updated_map=mark_points_on_map(points_list,map)
    answer=calculate_points_w_intersecting_lines(updated_map)
    print(answer)


type="main"
# type="test"

main(type)
