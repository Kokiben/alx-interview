#!/usr/bin/env python3
import sys
import signal

# Initialize variables
total_size = 0
status_codes_count = {
    '200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
    '404': 0, '405': 0, '500': 0
}
line_count = 0

def print_statistics():
    """Prints the current statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def process_line(line: str):
    """Processes a single line and updates the metrics if the format is correct."""
    global total_size, line_count
    
    try:
        parts = line.split()
        if len(parts) < 7:
            return
        
        # Extract file size and status code
        file_size = int(parts[-1])
        status_code = parts[-2]

        # Update total file size
        total_size += file_size

        # Update status code count if valid
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
        
        line_count += 1

    except Exception:
        pass  # If there's an error, just skip the line

def signal_handler(sig, frame):
    """Handles CTRL + C signal and prints the statistics before exiting."""
    print_statistics()
    sys.exit(0)

# Set up signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Read lines from stdin
try:
    for line in sys.stdin:
        process_line(line.strip())
        
        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics()
except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
