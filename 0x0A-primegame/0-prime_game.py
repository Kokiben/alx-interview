#!/usr/bin/python3

""" Prime Game Algorithm Python """

def is_prime(n):
    """ Checks if a number given n is a prime number """
    for j in range(2, int(n ** 0.5) + 1):
        if not n % j:
            return False
    return True

def calculate_primes(n, primes_list):
    """ Calculate all primes """
    top_prime = primes_list[-1]
    if n > top_prime:
        for j in range(top_prime + 1, n + 1):
            if is_prime(j):
                primes_list.append(j)
            else:
                primes_list.append(0)

def is_winner(x, nums):
    """
    x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """

    pr_w = {"Maria": 0, "Ben": 0}

    primes_list = [0, 0, 2]

    calculate_primes(max(nums), primes_list)

    for round_index in range(x):
        sum_options = sum((j != 0 and j <= nums[round_index])
                          for j in primes_list[:nums[round_index] + 1])

        if (sum_options % 2):
            winner = "Maria"
        else:
            winner = "Ben"

        if winner:
            pr_w[winner] += 1

    if pr_w["Maria"] > pr_w["Ben"]:
        return "Maria"
    elif pr_w["Ben"] > pr_w["Maria"]:
        return "Ben"

    return None
