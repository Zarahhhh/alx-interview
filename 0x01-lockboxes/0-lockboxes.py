#!/usr/bin/python3
"""
Module to determine if all lockboxes can be opened
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    - boxes: list of lists, each inner list contains keys to other boxes
    - returns: True if all boxes can be opened, else False
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    visited = set()  # set of boxes we've opened
    stack = [0]      # stack to hold boxes to explore; start with box 0

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            for key in boxes[current]:
                if 0 <= key < n and key not in visited:
                    stack.append(key)

    return len(visited) == n
