#!/usr/bin/python

# Day 4

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
# grabs raw string and converts it to list of ints
def sanitize_row(raw_row):
    formatted_row = raw_row.split(" ")
    formatted_row = [int(i.strip()) for i in formatted_row if i]
    return formatted_row

#-----------------------------------------------------
class bingo_board:
    def __init__(self, board):
        self.number_coordinates = {}            # Stores all numbers on board with thier respective coordinates e.g. 35: [3,4]
        self.column_bingo_tracker = [0] * 5     # each element is a counter for each column. When number is picked in a column, corresponding counter++
        self.row_bingo_tracker = [0] * 5        # each element is a counter for each row. When number is picked in a row, corresponding counter++
        self.won = False                        # Indicates if board won already

        #Load board
        for y, row in enumerate(board):
            for x, number in enumerate(row):
                self.number_coordinates[number] = [x,y]     # Numbers on board are keys and answer is their x,y coordinates
    
    # Function takes called number and checks board
    def check_number(self, called_number):
        if called_number in self.number_coordinates:
            self.column_bingo_tracker[self.number_coordinates[called_number][0]] += 1           # Increament counter for corresponding colomn
            self.row_bingo_tracker[self.number_coordinates[called_number][1]] += 1              # Increament counter for corresponding row

            row_check = self.row_bingo_tracker[self.number_coordinates[called_number][1]]       # If row corresponding counter gets to 5 = BINGO
            colum_check = self.column_bingo_tracker[self.number_coordinates[called_number][0]]  # If column corresponding counter gets to 5 = BINGO
            self.number_coordinates.pop(called_number)                                          # Remove any found numbers to faciliate procesing anwer at the end
            
            # Rather than looking at whole card, just look at the row and column counter that correspond to number coordinates
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

numbers_called = [int(n) for n in lines[0].split(',')]  # Ordered list of numbers being called for bingo
raw_boards = lines[3:]
temp_board = []
boards = []
answer_found = False

# Make Bingo board objects and store in list boards
for row in raw_boards:
    if row:
        temp_board.append(sanitize_row(row))
    else:
        boards.append(bingo_board(temp_board))
        temp_board = []
boards.append(bingo_board(temp_board))

for number in numbers_called:                                               # Call new number
    for it, board in enumerate(boards):                                     # Check each board for number
        if board.won == False and board.check_number(number) == "Bingo":    # If number in board with no win and it makes a bingo, process
            if answer_found == False:
                print("Part 1: ", board.get_solution(number))
                answer_found = True
            else: 
                part_2_answer = board.get_solution(number)
    #if answer_found: break                                                 # Used only for Part 1
print("Part 2: ", part_2_answer)


