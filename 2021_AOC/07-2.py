#! /usr/bin/env python3


def open_file_and_parse(test_or_main):
    #open correct file
    if test_or_main=="test":
        data=open("./data_07_test.txt")
    else:
        data=open("./data_07.txt")
    data=data.readlines()
    data=[int(x) for x in data[0].split(",")]
    return data

def find_possible_fuel_usage(location_list):
    i=0
    position_and_fuel=[]
    while i <= 999:
        distance=0
        fuel_used=0
        for location in location_list:
            distance=abs(location-i)
            j=1
            while j<=distance:
                fuel_used+=j
                j+=1
        position_and_fuel.append([i,fuel_used])
        i+=1
    return position_and_fuel

def find_best_spot(spot_list):
    best_spot=spot_list[0]
    for spot in spot_list:
        if spot[1]<best_spot[1]:
            best_spot=spot
    return best_spot


def main(type):
    data=open_file_and_parse(type)
    possibilities=find_possible_fuel_usage(data)
    best_spot=find_best_spot(possibilities)
    print(best_spot)



type="main"
# type="test"

main(type)