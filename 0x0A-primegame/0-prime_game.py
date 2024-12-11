#!/usr/bin/python3

""" prime game """


def _IsPrime(n):
    """ Check if `n` is prime. """
    for j in range(2, int(n ** 0.5) + 1):
        if not n % j:
            return False
    return True


def sieve_of_eratosthenes(n, primes):
    """ Extend `primes` with all primes up to `n`. """
    t_prm = primes[-1]
    if n > t_prm:
        for j in range(t_prm + 1, n + 1):
            if _IsPrime(j):
                primes.append(j)
            else:
                primes.append(0)


def isWinner(x, nums):
    """
    Determine the overall winner after `x` rounds.
    """

    plys_wns = {"Maria": 0, "Ben": 0}

    primes = [0, 0, 2]

    sieve_of_eratosthenes(max(nums), primes)

    for round in range(x):
        s_op = sum((j != 0 and j <= nums[round])
                          for j in primes[:nums[round] + 1])

        if (s_op % 2):
            winner = "Maria"
        else:
            winner = "Ben"

        if winner:
            plys_wns[winner] += 1

    if plys_wns["Maria"] > plys_wns["Ben"]:
        return "Maria"
    elif plys_wns["Ben"] > plys_wns["Maria"]:
        return "Ben"

    return None
