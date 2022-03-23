#! /usr/bin/env python3


class Point:
    def __repr__(self):
        return f"<find_at: {self.x}, {self.y} status: {self.status}>"

    discovered = "Discovered"
    explored = "Explored"
    undiscovered = "Undiscovered"

    @classmethod
    def get_min_discovered(cls,point_array):
        discovered_points = []
        path_hazards = []
        for row in point_array:
            for point in row:
                if point.status == point.discovered:
                    discovered_points.append([point, point.path_hazard])
                    path_hazards.append(point.path_hazard)
        min_path_hazard = min(path_hazards)
        for point_set in discovered_points:
            if point_set[0].path_hazard == min_path_hazard:
                return point_set[0]

    def __init__(self, x, y, hazard):
        if x == 0 and y == 0:
            self.status = self.discovered
            self.path_hazard = 0
        else:
            self.status = self.undiscovered
            self.path_hazard = 999999999999999999999
        self.x = x
        self.y = y
        self.hazard = hazard


def out_of_matrix_range(x, y, map):
    if 0 <= x < len(map[0]):
        if 0 <= y < len(map):
            return False
    return True


def explore_next_point(point_array):
    point_to_be_explored = Point.get_min_discovered(point_array)
    point_to_be_explored.status = point_to_be_explored.explored
    i = 0
    for row in point_array:
        for column in row:
            if column.status == column.explored:
                i += 1
    print(i, point_to_be_explored.x, point_to_be_explored.y, point_to_be_explored.path_hazard)
    for i in range(4):
        if i < 2:
            vector = 1
        else:
            vector = -1
        if i % 2 == 0:
            x_add = vector
            y_add = 0
        else:
            x_add = 0
            y_add = vector
        updated_x = point_to_be_explored.x + x_add
        updated_y = point_to_be_explored.y + y_add
        if out_of_matrix_range(updated_x, updated_y, point_array):
            continue
        point_to_be_discovered = point_array[updated_y][updated_x]
        if point_to_be_discovered.status == point_to_be_discovered.explored:
            continue
        point_to_be_discovered.path_hazard = min([point_to_be_discovered.path_hazard, point_to_be_explored.path_hazard + point_to_be_discovered.hazard])
        point_to_be_discovered.status = point_to_be_discovered.discovered


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
    data_expander = [[j + i for j in range(5)] for i in range(5)]
    large_data = []
    for expander_row in data_expander:
        j = 0
        for expander_column in expander_row:
            i = 0
            for row in data:
                if j == 0:
                    large_data.append([])
                for column in row:
                    large_data[expander_row[0] * len(data) + i].append((int(column) + expander_column - 1) % 9 + 1)
                i += 1
            j += 1
    point_array = []
    for i in range(len(large_data)):
        point_array.append([])
        for j in range(len(large_data[0])):
            point_array[i].append(Point(j, i, large_data[i][j]))
    return point_array


def main():
    points = open_file_and_parse(run_type)
    while True:
        explore_next_point(points)
        if points[-1][-1].status == points[-1][-1].discovered:
            break
    print(points[-1][-1].path_hazard)


run_type = "main"
# run_type = "temp"
# run_type = "test"

main()
