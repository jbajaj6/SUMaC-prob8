"""
Made by Jai Bajaj for the solution to problem 8c in the 2022 admissions exam
"""

from copy import deepcopy
from time import time

# get start time (to calculate time later)
t = time()

# get starting board (2s represent unfilled boxes)
# we can start with 0s in the center of each 3x3 because if there was a 1 there, there wouldn't be able to be another 1 in the 3x3
board = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 0, 2, 2, 0, 2, 2, 0, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 0, 2, 2, 0, 2, 2, 0, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 0, 2, 2, 0, 2, 2, 0, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2],
]

# function that retrieves all neighbors of a number in a matrix
def neighbors(a, row_number, column_number):
    return [[a[i][j] if i >= 0 and i < len(a) and j >= 0 and j < len(a[0]) else 0 for j in range(column_number-1, column_number+2)] for i in range(row_number-1, row_number+2)]

# checks if board is valid (by checking if it follows the two given rules)
def valid(board):
    # rule one
    # check if each row does has more than 7 0s and 2 1s
    for i in range(9):
        if board[i].count(0) > 7 or board[i].count(1) > 2:
            return False
    # check each column
    for i in range(9):
        col = [board[n][i] for n in range(9)]
        if col.count(0) > 7 or col.count(1) > 2:
            return False
    # check each box
    for box_x in range(3):
        for box_y in range(3):
            box = []
            for i in range(box_x * 3, box_x * 3 + 3):
                for j in range(box_y * 3, box_y * 3 + 3):
                    box.append(board[i][j])
            if box.count(0) > 7 or box.count(1) > 2:
                return False

    # rule two
    # check every box
    for row in range(9):
        for col in range(9):
            # if it is one, check if any neighbors are 1 too
            if board[row][col] == 1:
                # compile the numbers from the neighbors into one list
                n = neighbors(board, row, col)
                l = [i for i in n[0]]
                l.append(n[1][0])
                l.append(n[1][2])
                [l.append(i) for i in n[2]]
                # if a neighbor is also 1, the board is not valid
                if 1 in l:
                    return False
    return True

# check if the board is complete
def complete(board):
    for i in board:
        if 2 in i:
            return False
    return True

# find the next empty box
def findEmptyBox(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 2:
                return [row, column]
    return None

# create array of boards (3d)
boards = [board]

num_solutions = 0

# start decision tree loop
while True:
    # make sure the array has things in it
    if len(boards) == 0:
        break

    # get last board (for effienciency) and remove it from the list of boards
    current_board = boards[-1]
    boards.pop()

    # skip the rest if the current board is not valid
    if not valid(current_board):
        continue

    # check if board is still valid and not complete
    if valid(current_board) and not complete(current_board):
        # get first empty box in the board
        row, col = findEmptyBox(current_board)
        # find the possible options for that box
        possibilities = [0, 1]

        # add a new board the the list for every possiblity
        for i in possibilities:
            # make a deepcopy of the current board to mkae sure errors don't occur
            toAppend = deepcopy(current_board)
            # set the box to its possibility
            toAppend[row][col] = i
            # make sure the new board is still valid
            if valid(toAppend):
                boards.append(toAppend)
    # if the board is complete and valid, add one to the number of solutions
    if valid(current_board) and complete(current_board):
        num_solutions += 1

print(num_solutions)
print(time() - t)
