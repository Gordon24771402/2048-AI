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

