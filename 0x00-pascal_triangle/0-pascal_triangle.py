#!/usr/bin/python3
"""Module for Pascal's Triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]  # First row is just [1]

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the row before
        row = [1]  # Start every row with 1

        # Fill the middle numbers
        for j in range(1, i):
            num = prev_row[j - 1] + prev_row[j]
            row.append(num)

        row.append(1)  # End every row with 1
        triangle.append(row)

    return triangle
