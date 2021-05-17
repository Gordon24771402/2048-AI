import numpy as np
import random


# function to initialize 2048
def initialize():
    # create a 4x4 matrix containing zeros
    mat = np.zeros(shape=(4, 4), dtype='int')
    return mat


# function to add number at any random empty cell
def add(mat):
    # choose random index for row and column
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    # while loop breaks only if the cell is empty; otherwise chooses another pair of index
    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    # place either 2 or 4 at that empty random cell
    mat[r][c] = random.choice([2, 4])
    return mat


# function to check current state of 2048 (CONTINUE, WON, LOSE)
def check_state(mat):
    # if 2048 is achieved, return WON
    if 2048 in mat:
        return "WON"
    # if at least one empty cell, return CONTINUE
    if 0 in mat:
        return "CONTINUE"
    # if any two cells could get merged and create an empty cell, return CONTINUE
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return "CONTINUE"
    for j in range(3):
        # check edge cases
        if mat[3][j] == mat[3][j + 1]:
            return "CONTINUE"
    for i in range(3):
        # check edge cases
        if mat[i][3] == mat[i + 1][3]:
            return "CONTINUE"
    # else, return LOSE
    return "LOSE"
