#!/usr/bin/python3

import sys

def print_message(status_code_counts, total_file_size):
    """
    Method to print
    Args:
        status_code_counts: Dictionary of status codes
        total_file_size: Total size of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(total_file_size))
    for code, count in sorted(status_code_counts.items()):
        if count != 0:
            print("{}: {}".format(code, count))

status_code_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                      '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0
counter = 0

try:
    for line in sys.stdin:
        parts = line.split(" ")
        if len(parts) > 4:
            http_status_code = parts[-2]
            file_size = parts[-1]
            if http_status_code in status_code_counts:
                status_code_counts[http_status_code] += 1
            total_file_size += file_size
            line_count += 1
        if line_count == 10:
            line_count = 0
            print('File size: {}'.format(total_file_size))
            for code, count in sorted(status_code_counts.items()):
                if count != 0:
                    print('{}: {}'.format(code, count))
except Exception as error:
    pass
finally:
    print_message(dict_sc, total_file_size)
