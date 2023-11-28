#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    if not isinstance(grid, list):
        return 0

    perimeter = 0
    n = len(grid)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
