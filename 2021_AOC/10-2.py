#! /usr/bin/env python3




def open_file_and_parse(test_or_main):
    #open correct file
    if test_or_main=="test":
        data=open("./data_10_test.txt")
    elif test_or_main=="temp":
        data=open("./temp.txt")
    else:
        data=open("./data_10.txt")
    data=data.readlines()
    datum=[]
    for line in data:
        datum.append(line.strip())
    return datum

def look_for_corruption(data):
    score_list=[]
    for line in data:
        openers=[]
        score=0
        for element in line:
            if element=="<" or element=="(" or element=="[" or element=="{":
                openers.append(element)
            else:
                if element==")":
                    if openers[-1]!="(":
                        score+=3
                    openers.pop()       
                elif element=="]":
                    if openers[-1]!="[":
                        score+=57
                    openers.pop()
                elif element=="}":
                    if openers[-1]!="{":
                        score+=1197
                    openers.pop()
                elif element==">":
                    if openers[-1]!="<":
                        score+=25137
                    openers.pop()
        score_list.append(score)
    return score_list


def main(type):
    data=open_file_and_parse(type)
    score=look_for_corruption(data)
    print(score)
    print(sum(score))


# type="main"
# type="temp"
type="test"



main(type)
