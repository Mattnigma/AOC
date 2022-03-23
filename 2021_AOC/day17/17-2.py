#! /usr/bin/env python3

target_x = [x for x in range(117, 165)]
target_y = [y for y in range(-140, -88)]

possibility_count = 0
possibility_list = []
for init_vol_x in range(1, 165):
    for init_vol_y in range(-140, 140):
        temp_vol_x = init_vol_x
        temp_vol_y = init_vol_y
        x_pos = 0
        y_pos = 0
        continue_list = True
        while continue_list:
            x_pos += temp_vol_x
            y_pos += temp_vol_y
            if temp_vol_x > 0:
                temp_vol_x -= 1
            temp_vol_y -= 1
            if x_pos in target_x and y_pos in target_y:
                possibility_list.append([init_vol_x, init_vol_y])
                possibility_count += 1
                continue_list = False
            if x_pos > 164 or y_pos < -139:
                continue_list = False
for possibility in possibility_list:
    print(possibility)
print(possibility_count)