#!/usr/bin/python3

def canUnlockAll(boxes):
    # Total number of boxes
    n = len(boxes)
    # A set to keep track of unlocked boxes
    unlocked = set([0])
    # A list to act as a queue for boxes to be processed
    keys = [0]

    # While there are keys to process
    while keys:
        # Take the first key
        current_key = keys.pop()
        # Iterate through keys in the current box
        for key in boxes[current_key]:
            # If the key unlocks a new box, add it to the unlocked set and to the keys list
            if key not in unlocked and key < n:
                unlocked.add(key)
                keys.append(key)

    # Return True if all boxes have been unlocked, else False
    return len(unlocked) == n
