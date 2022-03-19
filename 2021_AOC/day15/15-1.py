#! /usr/bin/env python3


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


def map_path(floor_map, x, y, path, max_vals, hazard_list, hazard, back_count):
    path.append([x, y])
    hazard += floor_map[y][x]
    if x + 1 == max_vals[0] and y + 1 == max_vals[1]:
        # print(hazard)
        hazard_list.append(hazard)
        return hazard_list
    for i in range(4):
        if i < 2:
            vector = 1
        else:
            vector = -1
        if vector == -1:
            back_count += 1
        if back_count > 0:
            continue
        if i % 2 == 0:
            x_add = vector
            y_add = 0
        else:
            x_add = 0
            y_add = vector
        new_x = x + x_add
        new_y = y + y_add
        try:
            if new_x >= 0 and new_y >= 0:
                if [new_x, new_y] not in path:
                    hazard_list = map_path(floor_map, new_x, new_y, path.copy(), max_vals, hazard_list, hazard, back_count)
        except:
            pass
    return hazard_list


def find_paths(floor_map):
    x = 0
    y = 0
    path = []
    hazard_list = []
    hazard = -1 * floor_map[0][0]
    back_count = 0
    max_vals = len(floor_map[0]), len(floor_map)
    hazard_list = map_path(floor_map, x, y, path.copy(), max_vals, hazard_list, hazard, back_count)
    return hazard_list


def main():
    data = open_file_and_parse(run_type)
    hazard_list = find_paths(data)
    # print(hazard_list)
    print(min(hazard_list))


run_type = "main"
# run_type = "temp"
# run_type = "test"

main()
