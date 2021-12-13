#!/usr/bin/python

# Day 3

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
lines = load_input("input.txt", "str")


###### Part 1 ######
ones = [0] * 12
zeros = [0] * 12
gamma = ""
epsilon = ""

for line in lines:
    for it, digit in enumerate(line):
        if digit == '1': ones[it] += 1
        else: zeros[it] += 1

for it, digit in enumerate(ones):
    if zeros[it] > digit: 
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

most_common_start = gamma[0]
#Convert from binary to decimal
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print("Answer Part 1:", gamma * epsilon)

###### Part 2 ######
oxygen_candidates = []
co2_candidates = []

for line in lines:
    if line.startswith(most_common_start): oxygen_candidates.append(line)
    else: co2_candidates.append(line)

has_one = []
has_zero = []
digit_of_interest = 1
while len(oxygen_candidates) > 1:
    for candidate in oxygen_candidates:
        if candidate[digit_of_interest] == '1': has_one.append(candidate)
        else: has_zero.append(candidate)
    if len(has_zero) > len(has_one):
        oxygen_candidates = has_zero.copy()
    else: oxygen_candidates = has_one.copy()
    has_one = []
    has_zero = []
    digit_of_interest += 1

oxygen_answer = int(oxygen_candidates[0], 2)
print("done with oxygen", oxygen_answer)

has_one = []
has_zero = []
digit_of_interest = 1
while len(co2_candidates) > 1:
    for candidate in co2_candidates:
        if candidate[digit_of_interest] == '1': has_one.append(candidate)
        else: has_zero.append(candidate)
    if len(has_one) < len(has_zero): co2_candidates = has_one.copy()
    else: co2_candidates = has_zero.copy()
    has_one = []
    has_zero = []
    digit_of_interest += 1

co2_answer = int(co2_candidates[0], 2)
print("done with CO2", co2_answer)

print("Answer part 2: ", oxygen_answer * co2_answer)



