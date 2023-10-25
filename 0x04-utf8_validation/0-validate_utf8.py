#!/usr/bin/env python3
"""
UTF-8 validation module
"""


def validUTF8(data):
    """
    Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    trailing_bytes = 0

    for byte in data:
        # Check if it's a start byte
        if trailing_bytes == 0:
            # 1-byte character
            if (byte & 0b10000000) == 0:
                continue
            # 2-byte character
            elif (byte & 0b11100000) == 0b11000000:
                trailing_bytes = 1
            # 3-byte character
            elif (byte & 0b11110000) == 0b11100000:
                trailing_bytes = 2
            # 4-byte character
            elif (byte & 0b11111000) == 0b11110000:
                trailing_bytes = 3
            else:
                return False
        else:
            # Check if it's a trailing byte
            if (byte & 0b11000000) != 0b10000000:
                return False
            trailing_bytes -= 1

    # Ensure all expected trailing bytes were present
    return trailing_bytes == 0
