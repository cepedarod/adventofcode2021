#!/usr/bin/python

# Day 10
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

def part_1_answer(symbol):
    if symbol == ')': return 3
    elif symbol == ']': return 57
    elif symbol == '}': return 1197
    elif symbol == '>': return 25137
    return

def part_2_answer(symbol, current_total):
    new_score = current_total * 5

    if symbol == ')': new_score += 1
    elif symbol == ']': new_score += 2
    elif symbol == '}': new_score += 3
    elif symbol == '>': new_score += 4

    return new_score

def matching_char(symbol):
    if symbol == ')': return '('
    elif symbol == ']': return '['
    elif symbol == '}': return '{'
    elif symbol == '>': return '<'
    elif symbol == '(': return ')'
    elif symbol == '[': return ']'
    elif symbol == '{': return '}'
    elif symbol == '<': return '>'
    return
    
# When a closing symbol is found, this function check to find if there is a matching opening symbol
# If there is, the function will return nothing indicating its a valid string
# Otherwise, it will return the incorrect closing symbol
def validate_chunk(line_segment, closing_char, opener_indexes):
    target_opener = matching_char(closing_char)

    if target_opener not in opener_indexes or not opener_indexes[target_opener]:        # If there are no opening symbols that match the found closing symble, Line is invalid
        return closing_char

    elif not line_segment[opener_indexes[target_opener][-1] + 1:]:                      # If a matching opening symbol is found but nothing is enclosed between the opener and closer, symbol pair is legal
        opener_indexes[target_opener].pop()                                             # Once an opening symbol is accounted for, pop out of list to avoid double use
        return
    
    else:                                                                   # If a matching opening symbol is found and there are symbols enclosed between the opener and closer check that all inner symbols have a pair
                                                                            # Note we dont have to confirm validity of order because that has been done in previous passes    
        opener_counter = {'(':0, '{':0, '[':0, '<':0}
        closer_counter = {')':0, '}':0, ']':0, '>':0}
        inner_seg = line_segment[opener_indexes[target_opener][-1]+1:]      # Characters enclosed in opener/closer pair
        for symbol in line_segment[opener_indexes[target_opener][-1]+1:]:   # Count how many of each symbol there are in the inner string
            if symbol in opener_counter: opener_counter[symbol] += 1
            else: closer_counter[symbol] += 1
        
        for key in opener_counter.keys():
            if opener_counter[key] != closer_counter[matching_char(key)]: return closing_char   # If any of the opener and closer counts dont match, line is illegal
        opener_indexes[target_opener].pop()
        return


#-----------------------------------------------------
# MAIN CODE
#-----------------------------------------------------
# Open Input
lines = load_input("input.txt", "str")
total_score_1 = 0
part2_scores = []

for line in lines:
    opener_indexes = {'(':[], '{':[], '[':[], '<':[]}
    valid = True
    for it, item in enumerate(line):
        if item ==  ')' or item ==  ']' or item ==  '}' or item ==  '>':        # If closing symbol found, check for legal matching opening symbol
            invalid = validate_chunk(line[:it], item, opener_indexes)
            if invalid:
                total_score_1 += part_1_answer(invalid)
                #print("Invalid Line: ", line, "Invalid: ", invalid)
                valid = False
                break
        else:                                                                       # If opening symbol found, map its location for easy access when finding pair
            opener_indexes[item].append(it)
    # Part 2
    if valid:                                                                       # For all legal lines, figure out missing closers
        total_score_2 = 0
        unused_symbol_indexes = []                                                  # Indexes for all unpaired openers remain in unused_symbol_indexes
        for key in opener_indexes.keys():
            unused_symbol_indexes += opener_indexes[key]                            # Merge all unused index values in a single list and sort
        unused_symbol_indexes.sort(reverse = True)
        for i in unused_symbol_indexes:
            total_score_2 = part_2_answer(matching_char(line[i]), total_score_2)    # Missing symbols need to be ordered to match from last unpaired opener to earlierst unpaired opener
        part2_scores.append(total_score_2)

part2_scores.sort()
winning_index = int((len(part2_scores) -1) / 2)
print("Part 1 Answer: ", total_score_1)
print("Part 2 Answer: ", part2_scores[winning_index])