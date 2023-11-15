#!/usr/bin/python3
"""Module to validate UTF8
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding
    """
    skip = 0
    n = len(data)
    for i in range(n):
        pass