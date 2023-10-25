#!/usr/bin/python3

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        # Check if the current byte is a continuation byte (10xxxxxx)
        if 128 <= byte <= 191:
            if num_bytes == 0:
                return False
            num_bytes -= 1
        else:
            # Check the number of bytes needed to represent this character
            if num_bytes > 0:
                return False
            