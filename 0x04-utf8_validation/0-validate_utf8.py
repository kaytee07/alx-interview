#!/usr/bin/python3
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
        if trailing_bytes == 0:
            if (byte & 0b10000000) == 0:
                continue
            elif (byte & 0b11100000) == 0b11000000:
                trailing_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:
                trailing_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                trailing_bytes = 3
            else:
                return False
        else:
            if (byte & 0b11000000) != 0b10000000:
                return False
            trailing_bytes -= 1

    return trailing_bytes == 0
