#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determine the winner of each game round and the overall winner.
    Args:
        x (int): Number of rounds
        nums (list): Array of n values, where each represents the upper bound of integers in a round
    Returns:
        str or None: Name of the player with the most wins ("Maria" or "Ben"), or None if it's a tie.
    """
    if not nums or x < 1:
        return None


    def sieve_of_eratosthenes(max_n):
        """Generate a list of primes up to max_n using the Sieve of Eratosthenes."""
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        for i in range(2, int(max_n ** 0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, max_n + 1, i):
                    is_prime[multiple] = False
        return is_prime

    # Determine the maximum value of n to preprocess primes
    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)

    # Precompute the cumulative number of primes up to each n
    primes_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        primes_count[i] = primes_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round
    for n in nums:
        if primes_count[n] % 2 == 1:  # Odd number of primes means Maria wins
            maria_wins += 1
        else:  # Even number of primes means Ben wins
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
