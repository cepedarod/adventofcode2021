#!/usr/bin/python3

# Day 2


#-----------------------------------------------------
# FUNCTIONS
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


#-----------------------------------------------------
# MAIN CODE
#-----------------------------------------------------
# Open Input
lines = load_input('input.txt', "str")
'''''
###### Part 1 ######

forward = 0
depth = 0

for line in lines:
    if line.startswith("forward"): forward += int(line.split(" ")[1])
    elif line.startswith("down"): depth += int(line.split(" ")[1])
    elif line.startswith("up"): depth -= int(line.split(" ")[1])

print("Part 1 Answer: ", forward * depth)
'''

###### Part 2 ######

forward = 0
depth = 0
aim = 0

for line in lines:
    if line.startswith("forward"): 
        forward += int(line.split(" ")[1])
        depth += aim * int(line.split(" ")[1])
    elif line.startswith("down"): aim += int(line.split(" ")[1])
    elif line.startswith("up"): aim -= int(line.split(" ")[1])

print("Part 2 Answer: ", forward * depth)