#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.
    The perimeter is determined by counting the transitions between 
    land (1) and water (0) both horizontally and vertically.
    Args:
        grid (list of list of int): A rectangular grid where
        0 represents water and 1 represents land.
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    # Combine rows and columns using `zip` for vertical traversal
    for line in grid + list(map(list, zip(*grid))):
        # Count transitions between land and water
        for current_cell, next_cell in zip([0] + line, line + [0]):
            perimeter += int(current_cell != next_cell)
    return perimeter
