#!/usr/bin/python3
"""
N queens
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    Args:
        grid (list of list of int): A rectangular grid where
        0 represents water and 1 represents land.  
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all 4 possible edges
                if i == 0 or grid[i - 1][j] == 0:  # Top edge
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # Bottom edge
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Left edge
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # Right edge
                    perimeter += 1

    return perimeter
