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

def format_init_condit(init_data):
    i=0
    fish_of_age=[]
    while i<9:
        fish_of_age.append(0)
        i+=1
    for fish in init_data:
        fish_of_age[fish]+=1
    return fish_of_age



def day_of_groth(population):
    tomorrow_pop=[0 for i in range(9)]
    i=0
    while i<9:
        if i==0:
            tomorrow_pop[6]+=population[i]
            tomorrow_pop[8]+=population[i]
        else:
            tomorrow_pop[i-1]+=population[i]
        i+=1
    return tomorrow_pop

def main(type):
    init_fishes=open_file_and_parse(type)
    today_pop=format_init_condit(init_fishes)
    i=0
    while i<256:
        tomorrow_pop=day_of_groth(today_pop)
        today_pop=tomorrow_pop.copy()
        i+=1
    print(sum(today_pop))

type="main"
# type="test"

main(type)
