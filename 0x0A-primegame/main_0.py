#!/usr/bin/python3
isWinner = __import__('0-prime_game').isWinner

print(isWinner(3, [4, 5, 1]))  # Expected: Ben
print(isWinner(5, [2, 5, 1, 4, 3]))  # Expected: Ben
print(isWinner(1, [7]))  # Expected: Maria
print(isWinner(0, []))  # Expected: None
