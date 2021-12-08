#!/usr/bin/python

# Day 7

#-----------------------------------------------------
# MAIN CODE
#-----------------------------------------------------
# Open Input
with open("input.txt", 'r') as f:
    crab_pos = [int(i) for i in f.read().split(',')]

best = 999999999
total = 0
# The secret is that as you iterate, the total cost will reduce up until you hit the optiomal spot
# once the cost goes up instead of down, you know you reached the best lineup spot
# For part 2 look up Triangular numbers. Use that formula
for i in range(max(crab_pos) + 1):
    for sub in crab_pos:
        diff = abs(sub - i)
        diff = diff * (diff + 1) / 2            # Use only for part 2
        total += diff
    if total < best: 
        best = total
        total = 0
    else:
        print("Answer: ", best)
        break