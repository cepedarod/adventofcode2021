#!/usr/bin/python

# Day 9

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

# This is a recursive function that returns the size of the basin
def size_basin(depth, x, y, lines, checked_coordinates):
    basin_size = 1
    checked_coordinates.append((x,y))

    if int(depth) == 9: return 0    # 9s dont count towards basin

    # Check Left
    if x > 0:
        if int(lines[y][x-1]) > int(depth) and (x-1,y) not in checked_coordinates:
            basin_size += size_basin(lines[y][x-1], x-1, y, lines, checked_coordinates)
    # Check right
    if x < len(lines[0]) - 1:
        if int(lines[y][x+1]) > int(depth) and (x+1,y) not in checked_coordinates:
            basin_size += size_basin(lines[y][x+1], x+1, y, lines, checked_coordinates)
    # Check up
    if y > 0:
        if int(lines[y-1][x]) > int(depth) and (x,y-1) not in checked_coordinates:
            basin_size += size_basin(lines[y-1][x], x, y-1, lines, checked_coordinates)
    #Check down
    if y < len(lines) - 1:
        if int(lines[y+1][x]) > int(depth) and (x,y+1) not in checked_coordinates:
            basin_size += size_basin(lines[y+1][x], x, y+1, lines, checked_coordinates)
    
    return basin_size
    
#-----------------------------------------------------
# MAIN CODE
#-----------------------------------------------------
# Open Input
lines = load_input("input.txt", "str")

max_x_it = len(lines[0]) - 1
max_y_it = len(lines) - 1
sum_of_risk = 0
checked_coordinates = []
basins = []


for y, line in enumerate(lines):
    for x, number in enumerate(line):
        if (x == 0 and y == 0):
            if int(number) < int(line[x+1]) and int(number) < int(lines[y+1][x]):
                sum_of_risk += int(number) + 1
                basins.append(size_basin(number, x, y, lines, checked_coordinates))
        elif (x == 0 and y == max_y_it):
            if int(number) < int(line[x+1]) and int(number) < int(lines[y-1][x]):
                sum_of_risk += int(number) + 1
                basins.append(size_basin(number, x, y, lines, checked_coordinates))
        elif (x == max_x_it and y == 0):
            if int(number) < int(line[x-1]) and int(number) < int(lines[y+1][x]):
                sum_of_risk += int(number) + 1
                basins.append(size_basin(number, x, y, lines, checked_coordinates))
        elif y == 0:
            if int(number) < int(line[x-1]) and int(number) < int(line[x+1]) and int(number) < int(lines[y+1][x]):
                sum_of_risk += int(number) + 1
                basins.append(size_basin(number, x, y, lines, checked_coordinates))
        elif y == max_y_it:
            if int(number) < int(line[x-1]) and int(number) < int(line[x+1]) and int(number) < int(lines[y-1][x]):
                sum_of_risk += int(number) + 1
                basins.append(size_basin(number, x, y, lines, checked_coordinates))
        elif x == 0:
            if int(number) < int(line[x+1]) and int(number) < int(lines[y-1][x]) and int(number) < int(lines[y+1][x]):
                sum_of_risk += int(number) + 1
                basins.append(size_basin(number, x, y, lines, checked_coordinates))
        elif x == max_x_it:
            if int(number) < int(line[x-1]) and int(number) < int(lines[y-1][x]) and int(number) < int(lines[y+1][x]):
                sum_of_risk += int(number) + 1
                basins.append(size_basin(number, x, y, lines, checked_coordinates))
        else:
            if int(number) < int(line[x-1]) and int(number) < int(line[x+1]) and int(number) < int(lines[y-1][x]) and int(number) < int(lines[y+1][x]):
                sum_of_risk += int(number) + 1
                basins.append(size_basin(number, x, y, lines, checked_coordinates))

basins.sort(reverse = True)

print("Answer Part 1: ", sum_of_risk)
print("Answer Part 2: ", basins[0] * basins[1] * basins[2] )
        


