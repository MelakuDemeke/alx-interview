#!/usr/bin/python3
'''Module to validate UTF8'''


def validUTF8(data):
    '''
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: A list of integers representing bytes of data.
    :return: True if data is a valid UTF-8 encoding, else return False.
    '''
    # Number of bytes in the current UTF-8 character
    bytes_to_expect = 0

    for byte in data:
        if bytes_to_expect == 0:
            if byte < 128:
                continue
            elif byte < 224:
                bytes_to_expect = 1
            elif byte < 240:
                bytes_to_expect = 2
            elif byte < 248:
                bytes_to_expect = 3
            else:
                return False
        else:
            if byte < 128 or byte >= 192:
                return False
            bytes_to_expect -= 1

    return bytes_to_expect == 0
