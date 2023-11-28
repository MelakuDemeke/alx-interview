#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    if not isinstance(grid, list):
        return 0

    perimeter = 0
    n = len(grid)

    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
