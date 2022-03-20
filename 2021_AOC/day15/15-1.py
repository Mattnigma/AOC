#! /usr/bin/env python3
import copy

class Variables:
    def __init__(self):p


def open_file_and_parse(test_or_main):
    # open correct file
    if test_or_main == "test":
        data = open("./day15/test_data.txt")
    elif test_or_main == "temp":
        data = open("./misc/temp.txt")
    else:
        data = open("./day15/puzzle_data.txt")
    data = data.readlines()
    data = [i.strip() for i in data]
    data = [[int(j) for j in i] for i in data]
    return data


class MapPathParameters:
    floor_map: list[list[int]]
    x: int
    y: int
    path: list[list[int]]
    max_vals: tuple[int, int]
    hazard_list: list[int]
    hazard: int
    back_count: int


def map_path(p: MapPathParameters):
    p.path.append([p.x, p.y])
    p.hazard += p.floor_map[p.y][p.x]
    # test whether at end position (bottom right)
    if p.x + 1 == p.max_vals[0] and p.y + 1 == p.max_vals[1]:
        p.hazard_list.append(p.hazard)
        # print(len(p.hazard_list))
        return p.hazard_list
    for i in range(4):
        if i < 2:
            vector = 1
        else:
            vector = -1
        if vector == -1:
            p.back_count += 1
        if p.back_count > 0:
            continue
        if i % 2 == 0:
            x_add = vector
            y_add = 0
        else:
            x_add = 0
            y_add = vector
        new_x = p.x + x_add
        new_y = p.y + y_add
        try:
            if new_x >= 0 and new_y >= 0:
                if [new_x, new_y] not in p.path:
                    inner_p = copy.deepcopy(p)
                    inner_p.x = new_x
                    inner_p.y = new_y
                    p.hazard_list = map_path(inner_p)
        except:
            pass
    return p.hazard_list


def find_paths(floor_map):
    p = MapPathParameters()
    p.path = []
    p.floor_map = floor_map
    p.x = 0
    p.y = 0
    p.back_count = 0
    p.hazard = -1 * p.floor_map[0][0]
    p.hazard_list = []
    p.max_vals = len(p.floor_map[0]), len(p.floor_map)
    hazard_list = map_path(p)
    return hazard_list


def main():
    data = open_file_and_parse(run_type)
    hazard_list = find_paths(data)
    # print(hazard_list)
    print(min(hazard_list))
    # print(len(hazard_list))


# run_type = "main"
# run_type = "temp"
run_type = "test"

main()
