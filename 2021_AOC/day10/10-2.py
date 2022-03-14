#! /usr/bin/env python3




from statistics import median


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
        corruption=0
        for element in line:
            if element=="<" or element=="(" or element=="[" or element=="{":
                openers.append(element)
            else:
                if element==")":
                    if openers[-1]!="(":
                        corruption=1
                    openers.pop()       
                elif element=="]":
                    if openers[-1]!="[":
                        corruption=1
                    openers.pop()
                elif element=="}":
                    if openers[-1]!="{":
                        corruption=1
                    openers.pop()
                elif element==">":
                    if openers[-1]!="<":
                        corruption=1
                    openers.pop()
        i=len(openers)-1
        score_markers=[]
        if corruption==0:
            while i>=0:           
                if openers[i]=="(":
                    score_markers.append(1)
                elif openers[i]=="[":
                    score_markers.append(2)
                elif openers[i]=="{":
                    score_markers.append(3)
                elif openers[i]=="<":
                    score_markers.append(4)
                i-=1
            score=0
            for marker in score_markers:
                score=5*score+marker
            score_list.append(score)
    return score_list


def main(type):
    data=open_file_and_parse(type)
    score=look_for_corruption(data)
    print(score)
    print(median(score))


type="main"
# doc_type="temp"
# doc_type="test"



main(type)
