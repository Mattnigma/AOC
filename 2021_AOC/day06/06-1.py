#! /usr/bin/env python3

def open_file_and_parse(test_or_main):
    #open correct file
    if test_or_main=="test":
        data=open("./data_06_test.txt")
    else:
        data=open("./data_06.txt")
    data=data.readlines()
    data=[int(x) for x in data[0].split(",")]
    return data

def day_of_groth(population):
    tomorrow_pop=[]
    for fish in population:
        fish-=1
        if fish<0:
            tomorrow_pop.append(6)
            tomorrow_pop.append(8)
        else:
            tomorrow_pop.append(fish)
    population=tomorrow_pop.copy()
    return population

def main(type):
    today_pop=open_file_and_parse(type)
    i=0
    while i<80:
        tomorrow_pop=day_of_groth(today_pop)
        today_pop=tomorrow_pop.copy()
        i+=1
    print(len(today_pop))

type="main"
# doc_type="test"

main(type)
