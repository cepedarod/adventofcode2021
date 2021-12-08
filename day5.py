#!/usr/bin/python

# Day 5

#-----------------------------------------------------
# FUNCTIONS & Objects
#-----------------------------------------------------
def load_input(input_file, str_or_int):
    # Load input lines as a str
    if str_or_int == "str":
        with open(input_file, 'r') as f:
            lines = f.read().splitlines()
    #load input lines as ints
    else:
        with open(input_file, 'r') as f:
            lines = [int(number) for number in f.read().splitlines()]
    return lines

def normalize_direction(num_1, num_2):
    if num_2 < num_1: return num_2, num_1
    else: return num_1, num_2
#-----------------------------------------------------
# MAIN CODE
#-----------------------------------------------------
# Open Input
lines = load_input("input.txt", "str")

max_x = 0
max_y = 0
relevant_starts = []
relevant_ends = []
answer = 0

#### PART 1 ####
'''
for line in lines:
    start_coordinates = [int(i) for i in line.split(" -> ")[0].split(',')]
    end_coordinates = [int(i) for i in line.split(" -> ")[1].split(',')]

    if start_coordinates[0] > max_x: max_x = start_coordinates[0]
    if start_coordinates[1] > max_y: max_y = start_coordinates[1]
    if end_coordinates[0] > max_x: max_x = end_coordinates[0]
    if end_coordinates[1] > max_y: max_y = end_coordinates[1]
    
    
    if start_coordinates[0] == end_coordinates[0] or start_coordinates[1] == end_coordinates[1]:
        relevant_starts.append(start_coordinates)
        relevant_ends.append(end_coordinates)

sea_floor = [[0] * (max_y+1)  for _ in range(max_x + 1)]

for it, start_point in enumerate(relevant_starts):
    if start_point[0] == relevant_ends[it][0]:
        y_it, y_end = normalize_direction(start_point[1], relevant_ends[it][1])
        while y_it <= y_end:
            sea_floor[start_point[0]][y_it] += 1
            if sea_floor[start_point[0]][y_it] == 2: answer += 1
            y_it += 1
    
    else:
        x_it, x_end = normalize_direction(start_point[0], relevant_ends[it][0])
        while x_it <= x_end:
            sea_floor[x_it][start_point[1]] += 1
            if sea_floor[x_it][start_point[1]] == 2: answer += 1
            x_it += 1
    
print("Part 1:", answer)
'''
#### PART 2 ####
for line in lines:
    start_coordinates = [int(i) for i in line.split(" -> ")[0].split(',')]
    end_coordinates = [int(i) for i in line.split(" -> ")[1].split(',')]

    if start_coordinates[0] > max_x: max_x = start_coordinates[0]
    if start_coordinates[1] > max_y: max_y = start_coordinates[1]
    if end_coordinates[0] > max_x: max_x = end_coordinates[0]
    if end_coordinates[1] > max_y: max_y = end_coordinates[1]
    
    relevant_starts.append(start_coordinates)
    relevant_ends.append(end_coordinates)

sea_floor = [[0] * (max_y+1)  for _ in range(max_x + 1)]

for it, start_point in enumerate(relevant_starts):
    if start_point[0] == relevant_ends[it][0]:
        y_it, y_end = normalize_direction(start_point[1], relevant_ends[it][1])
        while y_it <= y_end:
            sea_floor[start_point[0]][y_it] += 1
            if sea_floor[start_point[0]][y_it] == 2: answer += 1
            y_it += 1
    
    elif start_point[1] == relevant_ends[it][1]:
        x_it, x_end = normalize_direction(start_point[0], relevant_ends[it][0])
        while x_it <= x_end:
            sea_floor[x_it][start_point[1]] += 1
            if sea_floor[x_it][start_point[1]] == 2: answer += 1
            x_it += 1
    
    else:
        x_it = start_point[0]
        x_end = relevant_ends[it][0]
        y_it = start_point[1]
        y_end = relevant_ends[it][1]

        if start_point[0] < relevant_ends[it][0]: x_dir = 1
        else: x_dir = -1
        if start_point[1] < relevant_ends[it][1]: y_dir = 1
        else: y_dir = -1

        while x_it != x_end:
            sea_floor[x_it][y_it] += 1
            if sea_floor[x_it][y_it] == 2: answer += 1
            x_it += x_dir
            y_it += y_dir
        sea_floor[x_it][y_it] += 1
        if sea_floor[x_it][y_it] == 2: answer += 1


print("Part 2:", answer)
