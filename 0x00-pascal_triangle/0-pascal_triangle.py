#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns Pascal’s triangle as a list of lists.
    Returns an empty list for n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of the triangle

    for a in range(1, n):
        row = [1]  # Every row starts with a 1
        for b in range(1, a):
            # Each element is the sum of the two elements above it
            row.append(triangle[a - 1][b - 1] + triangle[a - 1][b])
        row.append(1)  # Every row ends with a 1
        triangle.append(row)

    return triangle
