import numpy as np
from scipy import signal

def count_accessible_rollpaper(grid: list[int]) -> np.integer:
    grid_nd = np.array(grid)

    kernel = np.array([[-1, -1, -1],
                       [-1, 4, -1],
                       [-1, -1, -1]])
    convolved = signal.convolve2d(grid_nd, kernel, mode='valid')
    return np.sum(convolved > 0).astype(np.float64)

def main():
    grid = []
    # Turn the input into a 2d list with one layer of 0 padding:
    with open("D4_input.txt", "r") as f:
        for line_num, line in enumerate(f):
            line = line.strip()
            line_len = len(line)

            if line_num == 0:
                grid.append([0] * (line_len + 2))
            row = []
            row.append(0)
            for char in line:
                if char == '@':
                    row.append(1)
                elif char == '.':
                    row.append(0)
                else:
                    raise ValueError("char = {char}. Grid has to consist of '@' and '.'")
            row.append(0)
            grid.append(row)
        grid.append([0] * (line_len + 2))

    accessible_rollpaper_num = count_accessible_rollpaper(grid)
    print(accessible_rollpaper_num)
    print(type(accessible_rollpaper_num))

if __name__ == "__main__":
    main()
