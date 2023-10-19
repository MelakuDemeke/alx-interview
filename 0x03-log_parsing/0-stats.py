#!/usr/bin/python3

import sys

status_code_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                      '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0
line_count = 0

for line in sys.stdin:
    parts = line.split(" ")
    if len(parts) > 4:
        http_status_code = parts[-2]
        file_size = parts[-1]
        if http_status_code in status_code_counts:
                status_code_counts[http_status_code] += 1
        total_file_size += file_size
        line_count += 1
