#!/usr/bin/python3
"""
Prime Game
"""


def _IsPrime(n):
    """Check if a number n is prime.
    """
    pm = []
    s = [True] * (n + 1)
    for l in range(2, n + 1):
        if (s[l]):
            pm.append(l)
            for j in range(l, n + 1, l):
                s[j] = False
    return pm


def isWinner(x, nums):
    """Determine the overall winner after x rounds of the game.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for j in range(x):
        pm = _IsPrime(nums[j])
        if len(pm) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
