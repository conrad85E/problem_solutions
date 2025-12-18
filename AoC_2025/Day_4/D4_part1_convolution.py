"""
PURPOSE: Solution to "AoC 2025 Day 4: part 1"
METHOD: Convolution of NumPy Array using "Signal" module from SciPy
INPUT FILE: "D4_input.txt" (if not present -> refer to the link below)
PROBLEM STATEMENT: https://adventofcode.com/2025/day/4
"""

import numpy as np
from scipy import signal

def count_accessible_rollpaper(grid: list[int]) -> np.integer:
    '''
    Counts how many rolls of paper are immediatly removable by forklifts.
    A roll of paper is removable if it has less than 4 roll papers in its immediate neighborhood.
    
    :param grid: A grid of paper rolls where 0 is empty space and 1 is a paper roll.
    :type grid: list[int]
    :return: Number of all removable paper rolls.
    :rtype: integer[Any]
    '''
    # Turn the grid into numpy array
    grid_nd = np.array(grid)
    # This kernel will return:
    #   > 0: if a point on the grid has a paper roll AND it is removable
    #   <= 0: otherwise
    kernel = np.array([[-1, -1, -1],
                       [-1, 4, -1],
                       [-1, -1, -1]])
    # Perform convolution
    convolved = signal.convolve2d(grid_nd, kernel, mode='same')
    # Return the number of positive elements in the resulting convolution
    return np.sum(convolved > 0)

def main():
    grid = []
    # Turn the input into a 2d list:
    with open("D4_input.txt", "r") as f:
        for line in f:
            line = line.strip()
            row = []
            for char in line:
                if char == '@':
                    row.append(1)
                elif char == '.':
                    row.append(0)
                else:
                    raise ValueError("char = {char}. Grid has to consist of '@' and '.'")
            grid.append(row)


    accessible_rollpaper_num = count_accessible_rollpaper(grid)
    print(accessible_rollpaper_num)

if __name__ == "__main__":
    main()
