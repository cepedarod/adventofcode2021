#!/usr/bin/python3

# Day 1


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
lines = load_input('input.txt', "int")

'''
###### Part 1 ######
previous_depth = 0
depth_inc_counter = -1  # Counter starts at -1 to account for first depth > 0 check

for line in lines:
    if int(line) > previous_depth: depth_inc_counter += 1
    previous_depth = int(line)

print("Part 1 Answer: " + str(depth_inc_counter))
'''

###### Part 2 ######
depth_inc_counter = 0
previous_depth = sum(lines[0:3])
current_depths = lines[1:4]
lines = lines[4:]
while lines:
    current_depth_sum = sum(current_depths)
    current_depths.pop(0)
    current_depths.append(lines[0])
    lines.pop(0)
    if current_depth_sum > previous_depth: depth_inc_counter += 1
    previous_depth = current_depth_sum
if sum(current_depths) > previous_depth: depth_inc_counter += 1     # Check one last time since loop will end before final eval

print("Part 2 Answer: " + str(depth_inc_counter))