#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Checks if n is a positive integer and
        creates the first row of Pascal's triangle.
    '''
    if not isinstance(n, int) or n <= 0:
        return []

    triangle = [[1]]
    return triangle
