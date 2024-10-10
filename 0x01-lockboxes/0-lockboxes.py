#!/usr/bin/python3
"""
You have n locked boxes, numbered from 0 to n - 1, 
each potentially containing keys to other boxes.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    :param boxes: List of lists where each sublist contains keys to other boxes.
    :return: True if all boxes can be unlocked, otherwise False.
    """
    if not boxes or type(boxes) is not list:
        return False

    # Initialize a list of accessible boxes starting with box 0.
    accessible_boxes = [0]

    # Iterate over each accessible box and use its keys to unlock more boxes.
    for box_index in accessible_boxes:
        for key in boxes[box_index]:
            # If the key opens a box that hasn't been accessed yet, add it to the list.
            if key not in accessible_boxes and key < len(boxes):
                accessible_boxes.append(key)

    # Check if the number of accessible boxes matches the total number of boxes.
    return len(accessible_boxes) == len(boxes)
