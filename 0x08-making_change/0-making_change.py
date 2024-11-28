#!/usr/bin/python3
"""
minimize the number of coins used to sum up to the total
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of coin denominations.
        total (int): The target amount.

    Returns:
        int: The minimum number of coins needed, or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    # Initialize dp array with a value larger than any possible num of coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: no coins are needed to make total 0

    # Fill dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
