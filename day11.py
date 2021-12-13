#!/usr/bin/python

# Day 11
#-----------------------------------------------------
# FUNCTIONS & Objects
#-----------------------------------------------------
def load_input(input_file, str_or_int):
    if str_or_int == "str":                     # Load input lines as a str
        with open(input_file, 'r') as f:
            lines = f.read().splitlines()

    else:                                       # load input lines as ints
        with open(input_file, 'r') as f:
            lines = [int(number) for number in f.read().splitlines()]
    return lines

def flash( x, y, grid):
    flash_counter = 1
    grid[y][x] = 10
    
    # Check Left
    if x > 0:
        if grid[y][x-1] == 9: flash_counter += flash( x-1, y, grid)
        elif grid[y][x-1] != 10: grid[y][x-1] += 1
    # Check right
    if x < len(grid[0]) - 1:
        if grid[y][x+1] == 9: flash_counter += flash( x+1, y, grid)
        elif grid[y][x+1] != 10: grid[y][x+1] += 1
    # Check up
    if y > 0:
        if grid[y-1][x] == 9: flash_counter += flash( x, y-1, grid)
        elif grid[y-1][x] != 10: grid[y-1][x] += 1
    # Check down
    if y < len(grid) - 1:
        if grid[y+1][x] == 9: flash_counter += flash( x, y+1, grid)
        elif grid[y+1][x] != 10: grid[y+1][x] += 1
    # Check Top Left Corner
    if x > 0 and y > 0:
        if grid[y-1][x-1] == 9: flash_counter += flash( x-1, y-1, grid)
        elif grid[y-1][x-1] != 10: grid[y-1][x-1] += 1
    # Check Top Right Corner
    if x < len(grid[0]) - 1 and y > 0:
        if grid[y-1][x+1] == 9: flash_counter += flash( x+1, y-1, grid)
        elif grid[y-1][x+1] != 10: grid[y-1][x+1] += 1
    # Check Bottom Left Corner
    if x > 0 and y < len(grid) - 1:
        if grid[y+1][x-1] == 9: flash_counter += flash( x-1, y+1, grid)
        elif grid[y+1][x-1] != 10: grid[y+1][x-1] += 1
    # Check Bottom Right Corner
    if x < len(grid[0]) - 1 and y < len(grid) - 1:
        if grid[y+1][x+1] == 9: flash_counter += flash( x+1, y+1, grid)
        elif grid[y+1][x+1] != 10: grid[y+1][x+1] += 1
    
    return flash_counter
#-----------------------------------------------------
# MAIN CODE
#-----------------------------------------------------
# Open Input
lines = load_input("input.txt", "str")
total_flash_counter = 0
number_of_steps = 100
step = 0
part_2_found = False


grid = [[0] * 10  for _ in range(10)]

for y, line in enumerate(lines):
    for x, octopus in enumerate(line):
        grid[y][x] = int(octopus)


#while step < number_of_steps:
while part_2_found == False:
    flashing_octopus_count = 0
    for y, row in enumerate(grid):
        for x, octopus in enumerate(row):
            if octopus == 9: 
                flashing_octopus_count += flash(x,y,grid)
                total_flash_counter += flashing_octopus_count
            elif octopus != 10: grid[y][x] += 1
    
    for y, row in enumerate(grid):
        for x, octopus in enumerate(row): 
            if octopus == 10: grid[y][x] = 0
    
    if flashing_octopus_count == 100 and part_2_found == False:
        print("Part 2 Answer: ", step + 1)
        part_2_found = True
    step += 1
    if step == number_of_steps:
        print("Part 1 Answer: ", total_flash_counter)

