#!/usr/bin/python3
"""
Minimize the number of coins used to sum up to the total.
"""

def makeChange(coins, total):
    """
    Determine fewest number of coins needed to meet a given amount total.

    Uses dynamic programming to compute the minimum number of coins.

    Args:
        coins (list): A list of coin denominations.
        total (int): The target amount.

    Returns:
        int: The minimum number of coins needed, or  total.
    """
    if total == 0:
        return 0  # No coins are needed to make total 0

    # Initialize dp arr with a value larger than any possible num of coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: no coins are needed to make total 0

    # Iterate over each coin and update dp array for each possible amount
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return result for the total, or -1 if it's not possible to form total
    return dp[total] if dp[total] != float('inf') else -1
