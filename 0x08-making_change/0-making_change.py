#!/usr/bin/python3
"""
Minimize the number of coins used to sum up to the total.
"""

def makeChange(coins, total):
    # If the total is 0 or less, no coins are needed
    if total <= 0:
        return 0
    
    # Initialize the dp array with infinity, and dp[0] = 0 (base case)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Update the dp array for each coin
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still infinity, it means total cannot be made with the given coins
    if dp[total] == float('inf'):
        return -1
    
    return dp[total]
