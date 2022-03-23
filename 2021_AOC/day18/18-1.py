#! /usr/bin/env python3

from enum import Enum, unique, auto


@unique
class RunType(Enum):
    test = auto()
    temp = auto()
    main = auto()


def open_file_and_parse(run_type):
    # open correct file
    if run_type == RunType.test:
        data = open(f"./day{day}/test_data.txt")
    if run_type == RunType.temp:
        data = open("./misc/temp.txt")
    if run_type == RunType.main:
        data = open(f"./day{day}/puzzle_data.txt")
    data = data.readlines()
    data = [i.strip() for i in data]
    return data


def add_addends(addend_list: list) -> list:
    while len(addend_list) > 1:
        addend_0 = addend_list.pop(0)
        addend_1 = addend_list[0]
        addend_list[0] = [addend_0, addend_1]
        addend_list[0] = reduce_snailfish_number(addend_0)
    return addend_list[0]


def reduce_snailfish_number(snailfish_number: list, recursionlevel=0: int) -> list:
    complete = False
    while not complete:
        for sub_snailfish_number in snailfish_number:
            if type(sub_snailfish_number) == list:
                new subsnail, explode_left, explode_right = reduce_snailfish_number(sub_snailfish_number, recursionlevel + 1)


def main():
    parsed_data = open_file_and_parse(run_type)
    print(parsed_data)


day = 18
# run_type = RunType.main
# run_type = RunType.temp
run_type = RunType.test

main()