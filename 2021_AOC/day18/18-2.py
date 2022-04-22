#! /usr/bin/env python3

import copy
from enum import Enum, unique, auto


@unique
class RunType(Enum):
    test = auto()
    temp = auto()
    main = auto()


class SnailfishNumeral:
    def __init__(self, value, level, level_side):
        self.address = []
        for i in range(level):
            self.address.append(level_side[i])
        self.value = value
        self.depth = level

    def __repr__(self):
        return f"{self.value}@{self.address}"

    def prepare_for_add(self, side):
        self.address.insert(0, side)
        self.depth += 1
        return self


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
    snailfish_number_list = []
    for snailfish_num_string in data:
        snailfish_number_list.append(produce_snailfish_number(snailfish_num_string))
    return snailfish_number_list


def produce_snailfish_number(number_string):
    level = 0
    level_side = [0, 0, 0, 0, 0]  # 0 = right, 1 = left
    snailfish_number = []
    for char in number_string:
        if char == "[":
            level += 1
            level_side[level - 1] = 0
        elif char == ",":
            level_side[level - 1] = 1
        elif char == "]":
            level -= 1
        else:
            snailfish_number.append(SnailfishNumeral(int(char), level, level_side))
    return snailfish_number


def add_snailfish_numbers(snailfish_num_0, snailfish_num_1):
    new_snailfish_num = []
    for snailfish_numeral in snailfish_num_0:
        new_snailfish_num.append(snailfish_numeral.prepare_for_add(0))
    for snailfish_numeral in snailfish_num_1:
        new_snailfish_num.append(snailfish_numeral.prepare_for_add(1))
    new_snailfish_num = reduce_snailfish_num(new_snailfish_num)
    return new_snailfish_num


def reduce_snailfish_num(snailfish_num):
    i = 0
    while i < len(snailfish_num):
        if snailfish_num[i].depth == 5:
            if i > 0:
                snailfish_num[i-1].value += snailfish_num[i].value
            try:
                snailfish_num[i+2].value += snailfish_num[i+1].value
            except IndexError:
                pass
            snailfish_num.insert(i, SnailfishNumeral(0, 4, snailfish_num[i].address[0:4]))
            snailfish_num.pop(i+1)
            snailfish_num.pop(i+1)
            i = 0
        i += 1
    i = 0
    while i < len(snailfish_num):
        if snailfish_num[i].value > 9:
            temp = snailfish_num.pop(i)
            snailfish_num.insert(i, SnailfishNumeral(int((temp.value + temp.value % 2) / 2), temp.depth + 1, temp.address + [1]))
            snailfish_num.insert(i, SnailfishNumeral(int((temp.value - temp.value % 2) / 2), temp.depth + 1, temp.address + [0]))
            snailfish_num = reduce_snailfish_num(snailfish_num)
            return snailfish_num
        i += 1
    return snailfish_num


def make_magnitude_list(number_list):
    magnitude_list = []
    i = 0
    while i < len(number_list) - 1:
        j = 0
        while j < len(number_list):
            if i != j:
                sum_snailfish_num = add_snailfish_numbers(copy.deepcopy(number_list[i]), copy.deepcopy(number_list[j]))
                magnitude_list.append(find_magnitude(sum_snailfish_num))
            j += 1
        i += 1
    return magnitude_list


def find_magnitude(snailfish_number, depth = 4):
    i = 0
    while i < len(snailfish_number):
        if depth == 1:
            return snailfish_number[i].value * 3 + snailfish_number[i+1].value * 2
        if snailfish_number[i].depth == depth:
            magnitude_value = snailfish_number[i].value * 3 + snailfish_number[i+1].value * 2
            magnitude_depth = snailfish_number[i].depth - 1
            magnitude_address = snailfish_number[i].address[0:depth]
            snailfish_number.pop(i)
            snailfish_number.pop(i)
            snailfish_number.insert(i, SnailfishNumeral(magnitude_value, magnitude_depth, magnitude_address))
            i = 0
        i += 1
    snailfish_number = find_magnitude(snailfish_number, depth - 1)
    return snailfish_number


def main():
    parsed_data = open_file_and_parse(run_type)
    magnitude_list = make_magnitude_list(parsed_data)
    max_magnitude = max(magnitude_list)
    print(max_magnitude)


day = 18
run_type = RunType.main
# run_type = RunType.temp
# run_type = RunType.test

main()