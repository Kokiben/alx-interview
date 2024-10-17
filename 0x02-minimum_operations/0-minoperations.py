#!/usr/bin/python3
""" In a text file, there is a single character H """


def minOperations(target_count: int) -> int:
    """
    Calculatesmin num of opera needed to achieve exactly target_count H char.
    """
    # If target_count is less than 2, it's not more char through opr.
    if target_count < 2:
        return 0

    total_operations = 0
    current_divisor = 2

    # Loop through numbers starting from 2 to find factors of target_count.
    while current_divisor <= target_count:
        # If current_divisor is a factor of target_cou.
        # Keep dividing target_count by current_divisor until factor.
        while target_count % current_divisor == 0:
            total_operations += current_divisor
            target_count //= current_divisor
        # Move on to the next potential divisor.
        current_divisor += 1

    return total_operations
