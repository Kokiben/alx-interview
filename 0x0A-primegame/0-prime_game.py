#!/usr/bin/python3

""" prime game """


def is_prime(n):
    """Check if a number n is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes_up_to(n):
    """Generate a list of prime numbers up to n."""
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    """
    Determine the overall winner after x rounds of the game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the upper limit for each round.

    Returns:
        str: Name of the winner ("Maria", "Ben", or None if tied).
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = generate_primes_up_to(max_num)
    scores = {"Maria": 0, "Ben": 0}

    for num in nums:
        prime_count = sum(1 for p in primes if p <= num)
        if prime_count % 2 == 1:
            scores["Maria"] += 1
        else:
            scores["Ben"] += 1

    if scores["Maria"] > scores["Ben"]:
        return "Maria"
    elif scores["Ben"] > scores["Maria"]:
        return "Ben"
    return None

