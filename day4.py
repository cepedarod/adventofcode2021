#!/usr/bin/python

# Day 4

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

def sanitize_row(raw_row):
    formatted_row = raw_row.split(" ")
    formatted_row = [int(i.strip()) for i in formatted_row if i]
    return formatted_row

class bingo_board:
    def __init__(self, board):
        self.number_coordinates = {}
        self.column_bingo_tracker = [0] * 5
        self.row_bingo_tracker = [0] * 5
        self.won = False

        for y, row in enumerate(board):
            for x, number in enumerate(row):
                self.number_coordinates[number] = [x,y]
    
    def check_number(self, called_number):
        if called_number in self.number_coordinates:
            self.column_bingo_tracker[self.number_coordinates[called_number][0]] += 1
            self.row_bingo_tracker[self.number_coordinates[called_number][1]] += 1
            row_check = self.row_bingo_tracker[self.number_coordinates[called_number][1]]
            colum_check = self.column_bingo_tracker[self.number_coordinates[called_number][0]]
            self.number_coordinates.pop(called_number)
            
            if row_check == 5 or colum_check == 5:
                self.won = True
                return "Bingo"
        return ""

    def get_solution(self, number_called):
        solution = sum(self.number_coordinates.keys()) * number_called
        return solution


#-----------------------------------------------------
# MAIN CODE
#-----------------------------------------------------
# Open Input
lines = load_input("input.txt", "str")

numbers_called = [int(n) for n in lines[0].split(',')]
raw_boards = lines[3:]
temp_board = []
boards = []
answer_found = False

for row in raw_boards:
    if row:
        temp_board.append(sanitize_row(row))
    else:
        boards.append(bingo_board(temp_board))
        temp_board = []
boards.append(bingo_board(temp_board))

for number in numbers_called:
    for it, board in enumerate(boards):
        if board.won == False and board.check_number(number) == "Bingo":
            if answer_found == False:
                print("Part 1: ", board.get_solution(number))
                answer_found = True
            else: 
                part_2_answer = board.get_solution(number)
    #if answer_found: break                                     # Used only for Part 1
print("Part 2: ", part_2_answer)


