#!/usr/bin/python3
"""
Processing log data
"""

import sys

if __name__ == '__main__':

    total_size, line_counter = 0, 0
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    code_counts = {code: 0 for code in valid_codes}

    def display_metrics(metrics: dict, size: int) -> None:
        print("File size: {:d}".format(size))
        for code, count in sorted(metrics.items()):
            if count:
                print("{}: {}".format(code, count))

    try:
        for log_entry in sys.stdin:
            line_counter += 1
            log_parts = log_entry.split()
            if len(log_parts) < 7:
                continue
            try:
                # Parsing status code and file size
                status = log_parts[-2]
                file_size = int(log_parts[-1])

                if status in code_counts:
                    code_counts[status] += 1
                total_size += file_size
            except (ValueError, IndexError):
                continue

            if line_counter % 10 == 0:
                display_metrics(code_counts, total_size)

        display_metrics(code_counts, total_size)

    except KeyboardInterrupt:
        display_metrics(code_counts, total_size)
        raise
