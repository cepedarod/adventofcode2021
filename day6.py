#!/usr/bin/python

# Day 6

#-----------------------------------------------------
# FUNCTIONS & Objects
#-----------------------------------------------------

#-----------------------------------------------------
# MAIN CODE
#-----------------------------------------------------
# Open Input
fish = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
with open("input.txt", 'r') as f:
    for i in f.read().split(','): fish[int(i)] += 1

day = 0
it = 0
#end = 80       # Part 1
end = 256       # Part 2

while it < end:
    new_fish = fish[day]
    fish[day] += fish[7]
    fish[7] = fish[8]
    fish[8] = new_fish
    it += 1

    if day == 6: day = 0
    else: day += 1

answer = sum(fish.values())
print("Answer: ", answer)