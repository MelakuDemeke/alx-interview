#!/usr/bin/python3
""" Island Perimeter """

def island_perimeter(grid):
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
