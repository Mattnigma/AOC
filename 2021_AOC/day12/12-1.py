#! /usr/bin/env python3




class Cave:
    cavenames=[]
    end_count=0

    @classmethod
    def add_cavename(cls,cavename):
        cls.cavenames.append(cavename)

    def __init__(self,name):
        self.name = name
        if name == "start":
            self.type = "start"
        elif name == "end":
            self.type = "end"
        elif name.isupper()==True:
            self.type = "large"
        else:
            self.type = "small"
        self.connections=[]

    def __repr__(self):
        return f"<Cave.{self.name}>"


    def add_tunnel(self,destination):
        self.connections.append(destination)    

                



def explore_caves(starting_point,caves_traveled,path_list):
    # print(f'entering {starting_point}')
    caves_traveled.append(starting_point) # [ <Cave.start> ]
    if starting_point.name == "end":
        path_list.append(caves_traveled)
        return path_list
    for connection in starting_point.connections:
        if connection.doc_type == "start":
            pass
        elif connection.doc_type== "small" and connection in caves_traveled:
            pass
        else:
            path_list=explore_caves(connection,caves_traveled.copy(),path_list)
    return path_list



def open_file_and_parse(test_or_main):
    #open correct file
    if test_or_main=="test":
        data=open("./data_12_test.txt")
    elif test_or_main=="temp":
        data=open("./temp.txt")
    else:
        data=open("./data_12.txt")
    data=data.readlines()
    data=[i.strip().split("-") for i in data]
    return data

def init_caves(data):
    cave_list=[]
    for pair in data:
        for cave in pair:
            if cave not in Cave.cavenames:
                cave_list.append(Cave(cave))
                Cave.add_cavename(cave)
    return cave_list


def init_tunnels(data,cavelist,cavetionary):
    for cave in cavelist:
        for pair in data:
            if pair[0] == cave.name:
                cave.add_tunnel(cavetionary[pair[1]])
            if pair[1] == cave.name:
                cave.add_tunnel(cavetionary[pair[0]])

def create_cavetionary(cavelist):
    cavetionary={}
    for cave in cavelist:
        cavetionary[cave.name]=cave
    return cavetionary
                

def main(type):
    data=open_file_and_parse(type)
    cave_list=init_caves(data)
    cavetionary=create_cavetionary(cave_list)
    init_tunnels(data,cave_list,cavetionary)
    path_list=explore_caves(cavetionary["start"],["start"],[])
    # for cave in cave_list:
    #     for connection in cave.connections:
    #         print(cave.name + " -> " + connection.name)
    # for path in path_list:
    #     print(path)
    print(len(path_list))


type="main"
# doc_type="temp"
# doc_type="test"




main(type)
