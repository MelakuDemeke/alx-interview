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
            if 1 <= byte <= 127:
                num_bytes = 0
            elif 192 <= byte <= 223:
                num_bytes = 1
            elif 224 <= byte <= 239:
                num_bytes = 2
            elif 240 <= byte <= 247:
                num_bytes = 3
            else:
                return False
    
    # Check if there are any remaining bytes to complete a character
    return num_bytes == 0
