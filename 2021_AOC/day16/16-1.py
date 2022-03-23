#! /usr/bin/env python3

from enum import Enum, unique, auto


@unique
class RunType(Enum):
    test1 = 1
    test2 = 2
    test3 = 3
    test4 = 4
    temp = auto()
    main = auto()


def open_file_and_parse(run_type):
    # open correct file
    if run_type == RunType.test1:
        data = open(f"./day{day}/test_data_1.txt")
    if run_type == RunType.test2:
        data = open(f"./day{day}/test_data_2.txt")
    if run_type == RunType.test3:
        data = open(f"./day{day}/test_data_3.txt")
    if run_type == RunType.test4:
        data = open(f"./day{day}/test_data_4.txt")
    if run_type == RunType.temp:
        data = open("./misc/temp.txt")
    if run_type == RunType.main:
        data = open(f"./day{day}/puzzle_data.txt")
    data = data.readlines()
    data = data[0].strip()
    return data


# use for one digit hexadecimal numbers
def convert_hexdec_to_bin(problem_hexdec: str) -> str:
    problem_binary = ""
    for input_str in problem_hexdec:
        deci = int(input_str, 16)
        character_bin = ""
        for i in range(3, -1, -1):
            if deci >= 2 ** i:
                character_bin += "1"
                deci -= 2 ** i
            else:
                character_bin += "0"
        problem_binary += character_bin
    return problem_binary


def find_packet_list(binary: str, repeat = True) -> tuple:
    version_total = 0
    packet_length = 0
    while True:
        if len(binary) >= 11:
            version = int(binary[0:3], 2)
            type_ID = int(binary[3:6], 2)
            binary = binary[6:]
            version_total += version
            if type_ID == 4:
                this_packet_contents = ""
                packet_continue = True
                packet_length += 6
                while packet_continue:
                    binary_digits = binary[0:5]
                    binary = binary[5:]
                    this_packet_contents += binary_digits[1:]
                    if not int(binary_digits[0]):
                        packet_continue = False
                    packet_length += 5
                this_packet_contents = int(this_packet_contents, 2)
            if type_ID != 4:
                length_type_ID = int(binary[0])
                binary = binary[1:]
                if not length_type_ID:
                    packet_contents_length = int(binary[0: 15], 2)
                    this_packet_contents = binary[15: 15 + packet_contents_length]
                    binary = binary[15 + packet_contents_length:]
                    packet_length += packet_contents_length + 22
                    a, b, c, recursive_version_addend = find_packet_list(this_packet_contents)
                    version_total += recursive_version_addend
                if length_type_ID:
                    packets_contained = int(binary[0:11], 2)
                    binary = binary[11:]
                    this_packet_contents = ""
                    for i in range(packets_contained):
                        a, b, inner_packet_length, recursive_version_addend = find_packet_list(binary, False)
                        version_total += recursive_version_addend
                        this_packet_contents += binary[:inner_packet_length]
                        binary = binary[inner_packet_length:]
                    packet_length += 18 + len(this_packet_contents)
        else:
            packet_length += len(binary)
            break
        if not repeat:
            if len(binary) < 7:
                packet_length += len(binary)
            break
    return this_packet_contents, version, packet_length, version_total





def main():
    parsed_data = open_file_and_parse(run_type)
    binary_data = convert_hexdec_to_bin(parsed_data)
    this_packet_contents, version, packet_length, version_total = find_packet_list(binary_data)
    print(version_total, this_packet_contents, version, packet_length)


day = 16
run_type = RunType.main
# run_type = RunType.temp
# run_type = RunType.test1
# run_type = RunType.test2
# run_type = RunType.test3
# run_type = RunType.test4

main()
