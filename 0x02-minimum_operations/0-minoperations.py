#!/usr/bin/env python3
'''
This script defines a function to compute the fewest number of operations
needed to result in exactly n 'H' characters. It provides an efficient
approach to achieving this by simulating copy and paste operations.
'''


def minOperations(n):
    ''''
    Computes the fewest number of operations needed to result
    in exactly n 'H' characters.

    :param n: The target number of 'H' characters.
    :return: The minimum number of operations required.
    '''
    if not isinstance(n, int):
        return 0

    operation_count = 0
    clipboard_contents = 0
    complet = 1

    while complet < n:
        if clipboard_contents == 0:
            clipboard_contents = complet
            complet += clipboard_contents
            operation_count += 2
        elif n - complet > 0 and (n - complet) % complet == 0:
            clipboard_contents = complet
            complet += clipboard_contents
            operation_count += 2
        elif clipboard_contents > 0:
            complet += clipboard_contents
            operation_count += 1
    return operation_count
