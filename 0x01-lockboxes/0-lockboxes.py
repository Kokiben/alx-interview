#!/usr/bin/python3
"""
You have n locked boxes, numbered from 0 to n - 1.
Each box may contain keys to other boxes.
"""


def canUnlockAll(boxes):
    """
    Checks if all boxes can be opened.

    :param boxes: A list of lists containing keys to other boxes.
    :return: True if all boxes can be unlocked, otherwise False.
    """
    if not boxes or type(boxes) is not list:
        return False

    opened = [0]
    for box in opened:
        for key in boxes[box]:
            if key not in opened and key < len(boxes):
                opened.append(key)
    if len(opened) == len(boxes):
        return True
    return False
