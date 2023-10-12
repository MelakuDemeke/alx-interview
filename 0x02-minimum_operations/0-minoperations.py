#!/usr/bin/env python3

def minOperations(n):
    if not isinstance(n, int) or n <= 0:
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
