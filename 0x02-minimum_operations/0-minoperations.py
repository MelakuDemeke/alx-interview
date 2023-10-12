#!/usr/bin/env python3

def minOperations(n):
    if not isinstance(n, int) or n <= 0:
        return 0 

    operation_count = 0
    clipboard_contents = 0

    while n > 1:
        pass