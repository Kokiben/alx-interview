#!/usr/bin/python3
"""
method determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    # Masks to identify leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000
    for num in data:
        # Get the 8 least significant bits
        byte = num & 0xFF
        if num_bytes == 0:
            # Determine the number of bytes in this character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1
            # 1 byte char (0xxxxxxx) or invalid if more than 4 bytes
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # If this byte is not a continuation byte (10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False
        num_bytes -= 1
    # If we complete all bytes, num_bytes should be zero
    return num_bytes == 0
