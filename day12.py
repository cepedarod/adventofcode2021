#!/usr/bin/python

# Day 12
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
 
# This functions recurses through the cave nodes to find viable paths
    # Cave is the node being explored
    # Caves is a dict that maps all caves and what other nodes they connect to
    # visited_caves keeps track of what nodes have been passed by already
    # path is a debug variable to be able to print the valid path found
    # part_2_rule_met is used to determin if a small cave can be visited twice
def explore(cave, caves, visited_caves, path, part_2_rule_met):
    viable_path_counter = 0
    path += "-" + cave

    # make sure this stop is registered in the visited_caves list
    if cave not in visited_caves: visited_caves[cave] = 1
    else: visited_caves[cave] += 1

    # Main exploration loop
    for hop in caves[cave]:
        if hop == 'end':                # If the next hop is the end, record valid path
            path += "-end"
            viable_path_counter += 1
            #print(path)                # DEBUG
        elif hop.isupper() == True:     # If next cave is a large cave, continue exploring
            viable_path_counter += explore(hop, caves, visited_caves.copy(), path, part_2_rule_met)
        elif hop != "start" and hop not in visited_caves:                                               # If next cave is a small cave that has never been visited, explore
            viable_path_counter += explore(hop, caves, visited_caves.copy(), path, part_2_rule_met)
        elif hop != "start" and part_2_rule_met == False:                                               # If next cave is small and HAS been visited, explore only if no other small cave has been visited twice
            viable_path_counter += explore(hop, caves, visited_caves.copy(), path, True)                # part_2_rule_met set to True to avoid double dipping
    
    return viable_path_counter

#-----------------------------------------------------
# MAIN CODE
#-----------------------------------------------------
# Open Input
lines = load_input("input.txt", "str")
caves = {}
visited_caves = {}
answer = 0

# Make sure all caves are mapped in caves dict
for line in lines:
    if line.split('-')[0] in caves:
        caves[line.split('-')[0]].append(line.split('-')[1])
    else:
        caves[line.split('-')[0]] = [line.split('-')[1]]

    if line.split('-')[1] in caves:
        caves[line.split('-')[1]].append(line.split('-')[0])
    else:
        caves[line.split('-')[1]] = [line.split('-')[0]]

# recurse though caves to find answers
for cave in caves["start"]:
    #answer += explore(cave, caves, visited_caves, "start", True)       # Use for part 1
    answer += explore(cave, caves, visited_caves, "start", False)       # Use for part 2
    visited_caves = {}

print("Answer: ", answer)
