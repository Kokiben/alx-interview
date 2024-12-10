#!/usr/bin/python3
"""
 the perimeter of the island
"""


def island_perimeter(grid):
    """
     Return : The perimeter of the island.
    grid:(list of list of int): A rectangular grid where
    0 represents water and 1 represents land.
    """
    peri = 0
    for line in grid + list(map(list, zip(*grid))):
        for a, b in zip([0] + line, line + [0]):
            peri += int(a != b)
    return peri
