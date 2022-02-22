#! /usr/bin/env python3


def open_file_and_parse(test_or_main):
    #open correct file
    if test_or_main=="test":
        data=open("./data_08_test.txt")
    elif test_or_main=="temp":
        data=open("./temp.txt")
    else:
        data=open("./data_08.txt")
    data=data.readlines()
    data=[i.split("|") for i in data]
    i=0
    while i < len(data):
        data[i]=[data[i][j].strip().split() for j in range(len(data[i]))]
        i+=1
    return data

def count_unique_numbers(data):
    unique_digit_count=0
    for set in data:
        for digit in set[1]:
            if len(digit)==2 or len(digit)==3 or len(digit)==4 or len(digit)==7:
                unique_digit_count+=1
    return unique_digit_count

def main(type):
    data=open_file_and_parse(type)
    unique_numbers=count_unique_numbers(data)
    print(unique_numbers)
    #print(data)




type="main"
# type="temp"
# type="test"



main(type)
