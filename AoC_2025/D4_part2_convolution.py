"""
PURPOSE: Solution to "AoC 2025 Day 4: part 2"
METHOD: Convolution of NumPy Array using "Signal" modult from SciPy
INPUT FILE: "D4_input.txt" (if not present -> refer to the link below)
PROBLEM LINK: https://adventofcode.com/2025/day/4 
"""

import numpy as np
from scipy import signal

def count_accessible_rollpaper(grid: list[int]) -> np.integer:
    '''
    Counts how many rolls of paper are removable by forklifts after repeating the process of removing.
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
    removed_rollpaper_sum = np.int64(0)
    
    while True:
        # Step 1: Perform convolution with 1-layer zero-padding
        convolved_grid = signal.convolve2d(grid_nd, kernel, mode='same')
        # Step 2: Count positive numbers in the convolved output
        rollpaper_to_remove = convolved_grid > 0
        curr_pass_removed_rollpaper_sum = np.sum(rollpaper_to_remove)
        # Step 3: If no positives (no removable paper rolls) -> return accumulated sum
        if curr_pass_removed_rollpaper_sum == 0:
            return removed_rollpaper_sum
        # Step 4: Accumulate number of removable paper rolls
        removed_rollpaper_sum += curr_pass_removed_rollpaper_sum
        # Step 5: Remove removable paper rolls from the grid
        grid_nd -= rollpaper_to_remove

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
    

    num_accessible_rollpaper = count_accessible_rollpaper(grid)
    print(num_accessible_rollpaper)

if __name__ == "__main__":
    main()
