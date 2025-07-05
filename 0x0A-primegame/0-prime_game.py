#!/usr/bin/python3
"""Module for Prime Game algorithm"""


def isWinner(x, nums):
    if not nums or x < 1:
        return None

    # Find the maximum number in nums
    max_num = max(nums)

    # Step 1: Create a list of prime counts up to max_num using the sieve
    primes = [0] * (max_num + 1)
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, max_num + 1):
        if is_prime[i]:
            for j in range(i * 2, max_num + 1, i):
                is_prime[j] = False
        primes[i] = primes[i - 1] + (1 if is_prime[i] else 0)

    # Step 2: Play the game for each round and count wins
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Step 3: Return who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
