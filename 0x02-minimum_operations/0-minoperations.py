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

    while n > 1:
        if n % 2 == 0:
            # If n is even, perform a paste operation
            clipboard_contents += 1
            n //= 2
        else:
            # If n is odd, perform a copy-all and paste operation
            clipboard_contents += n
            n //= 2
        operation_count += 1
    return operation_count
