#!/usr/bin/python3
"""
This module defines the isWinner function used to determine
the winner of a prime game between Maria and Ben.
"""


def isWinner(x, nums):
    """
    Determines the winner of a prime game played over x rounds.

    Parameters:
    x (int): Number of rounds.
    nums (list of int): The upper limit of numbers for each round.

    Returns:
    str or None: The name of the player with the most wins ("Maria" or "Ben"),
    or None if the winner cannot be determined.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    sieve = [True for _ in range(max_n + 1)]
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    prime_counts = [0] * (max_n + 1)
    count = 0
    for i in range(1, max_n + 1):
        if sieve[i]:
            count += 1
        prime_counts[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
