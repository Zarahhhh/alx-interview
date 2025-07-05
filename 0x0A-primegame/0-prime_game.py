#!/usr/bin/python3


def isWinner(x, nums):
    if not nums or x < 1:
        return None

    max_n = max(nums)
    sieve = [True for _ in range(max_n + 1)]
    sieve[0] = sieve[1] = False

    # Sieve of Eratosthenes to find all primes up to max_n
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    # Precompute number of primes up to each number 0 to max_n
    prime_counts = [0] * (max_n + 1)
    count = 0
    for i in range(1, max_n + 1):
        if sieve[i]:
            count += 1
        prime_counts[i] = count

    # Determine winner for each round
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
    else:
        return None
