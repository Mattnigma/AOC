#! /usr/bin/env python3

class Point:

    def __repr__(self):
        return f"<Point.{self.x_val},{self.y_val}>"

    def __init__(self,x_val,y_val):
        self.x_val=x_val
        self.y_val=y_val

    def fold_point(self,fold):
        fold_int=int(fold[1])
        if fold[0]=="x":
            if self.x_val > fold_int:
                self.x_val= 2 * fold_int - self.x_val
        if fold[0]=="y":
            if self.y_val > fold_int:
                self.y_val= 2 * fold_int - self.y_val



def open_file_and_parse(test_or_main):
    #open correct file
    if test_or_main=="test":
        data=open("./data_13_test.txt")
    elif test_or_main=="temp":
        data=open("./temp.txt")
    else:
        data=open("./data_13.txt")
    data=data.readlines()
    data=[i.strip().split() for i in data]
    points , folds=get_points_folds(data)
    return points , folds


def get_points_folds(data):
    points=[]
    folds=[]
    for list in data:
        if list==[]:
            pass
        elif "=" in list[-1]:
            folds.append(list[-1].split("="))
        else:
            points.append(list[0].split(","))
    return points , folds


def init_points(point_string_list):
    point_list=[]
    for point_string in point_string_list:
        point_list.append(Point(int(point_string[0]),int(point_string[1])))
    return point_list


def fold_points(point_list,fold):
    for point in point_list:
        point.fold_point(fold)
    new_point_list=[]
    point_coordinate_list=[]
    for point in point_list:
        point_coordinates=[point.x_val , point.y_val]
        if point_coordinates not in point_coordinate_list:
            new_point_list.append(point)
            point_coordinate_list.append(point_coordinates)
    return new_point_list


def generate_graph():
    graph=[]
    for i in range(6):
        graph.append([])
        for j in range(39):
            graph[i].append(" ")
    return graph


def map_points_to_map(graph, point_list):
    for point in point_list:
        graph[point.y_val][point.x_val]="H"
    return graph


def main(type):
    point_string_list , fold_list = open_file_and_parse(type)
    point_list = init_points(point_string_list)
    for fold in fold_list:
        point_list=fold_points(point_list , fold)
    graph=generate_graph()
    graph=map_points_to_map(graph , point_list)
    for line in graph:
        print(line)



type="main"
# type="temp"
# type="test"



main(type)
