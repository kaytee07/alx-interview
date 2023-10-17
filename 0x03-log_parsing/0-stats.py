#!/usr/bin/python3
"""
read stdin line ny line and compute metrics
"""
import sys
import re


def parse_line(line):
    """
    parse line based on specified format of input
    """
    format = (
        r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET \/projects\/260 '
        r'HTTP\/1\.1" (\d+) (\d+)'
    )
    match = re.match(format, line)
    if match:
        return int(match.group(2)), int(match.group(3))
    return None


def print_stats(total_file_size, status_codes):
    """
    print status code and number of lines it appears on
    """
    print(f'File size: {total_file_size}')
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code]:
            print(f"{status_code}: {status_codes[status_code]}")


def main():
    """
    print status code and number of lines it was found in
    """
    total_file_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parsed_data = parse_line(line)
            if parsed_data:
                status_code, file_size = parsed_data
                total_file_size += file_size
                status_codes[status_code] += 1
                line_count += 1

            if line_count % 10 == 0:
                print_stats(total_file_size, status_codes)
    except KeyboardInterrupt:
        pass

    print_stats(total_file_size, status_codes)


if __name__ == '__main__':
    main()
