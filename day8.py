#!/usr/bin/python

# Day 8
# 1 =  2 | 7 = 3 | 4 = 4 | 8 = 7
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

#-----------------------------------------------------
# MAIN CODE
#-----------------------------------------------------
# Open Input
lines = load_input("input.txt", "str")
answer = 0
grand_total = 0

'''
#### PART 1 ####
for line in lines:
    for digit in line.split(" | ")[1].split(' '):
        if len(digit) <= 4 or len(digit) == 7: answer += 1

print("Answer: ", answer)
'''
#### PART 2 ####
# Step 0: EEEVERYTHING below will need to be repeated for every line of the input
for line in lines:
# Reset all variables before processing line
    seg_map = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': '',}
    length_grouping = {2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
    digit_representation = {0:"", 1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:""}
    digits_found = 0
    output_list = []
    input_list = []
    input_list.append(line.split(" | ")[0].split(' '))
    output_list.append(line.split(" | ")[1].split(' '))

# Step 1: group all options by number of segments used, find all unique mappings and Find the 1 and the 7 to determine what 'a' maps to
    for input in input_list:
        for digit in input:
            length_grouping[len(digit)].append(digit)
            if len(digit) == 2: digit_representation[1] = digit
            elif len(digit) == 3: digit_representation[7] = digit
            elif len(digit) == 4: digit_representation[4] = digit
            elif len(digit) == 7: digit_representation[8] = digit

    seg_map['a'] = list(set(digit_representation[7])-set(digit_representation[1]))[0]

# Step 2: using 4 and knowledge of what the 'a' segment is find 9
# This works because 9 is the only 6-segment digit that is only segment off from the 4 digit with the a segment added
# This also determines what the e segment maps to
    diff = digit_representation[4] + seg_map['a']
    for it, number in enumerate(length_grouping[6]):
        if len(set(number) - set(diff)) == 1:
            digit_representation[9] = number
            seg_map['g'] = list(set(number) - set(diff))[0]
            length_grouping[6].pop(it)                          # Remove 9 from this list as it is solved
            break

# Step 3: knowing 9, use 1 to determine 0 and 6
# 0 has 4 different segments than 1 and 6 has 5 different segments than 1
    for number in length_grouping[6]:
        if len(set(number) - set(digit_representation[1])) == 4: digit_representation[0] = number
        else: digit_representation[6] = number

# Step 4: knowing what 0 and 6 look like you can diff 8 with 6 to determine the mapping for 'c'
#         and you can dif 8 with 0 to determine what d is
    seg_map['c'] = list(set(digit_representation[8])-set(digit_representation[6]))[0]
    seg_map['d'] = list(set(digit_representation[8])-set(digit_representation[0]))[0]

#step 5: knowing what c maps to, you can use 1 to determine what f maps to
    seg_map['f'] = digit_representation[1].replace(seg_map['c'], '')

# step 6: only the 5 segment digits remain to decypher
# of the 4 5-segment digits we only know all the segments used for 3
    is_three = True
    for it, number in enumerate(length_grouping[5]):
        for segment in list(number):
            if segment not in seg_map.values(): 
                is_three = False
                break
        if is_three == True: 
            digit_representation[3] = number
            length_grouping[5].pop(it)          # Remove 3 from this list as it is solved
        else: is_three = True 

# Step 7: 2 and 5 are the only numbers left to crack. Of the 2, only 5 has the known segment f
#         Use f to find 5 and consequently 2
    for number in length_grouping[5]:
        if seg_map['f'] in number: digit_representation[5] = number
        else: digit_representation[2] = number

# Step 8: all numbers have been deciphered. now to get the asnwer
#         to best decode the outputs we first need to flip the keys and values from digit_representation
#         After that is done, iterate through the output and sum the totals
    d = ''
    digit_decoder = dict([(value, key) for key, value in digit_representation.items()])
    for output in output_list:
        for digit in output:
            for key in digit_decoder.keys():
                if len(key) == len(digit) and len(set(key) - set(digit)) == 0: 
                    d += str(digit_decoder[key])
                    break
        grand_total += int(d)

print("Answer: ", grand_total)

