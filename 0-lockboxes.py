#!/usr/bin/python3
"""
unlock all boxes with available keys
"""


def canUnlockAll(boxes):
    """
    unlock all boxes
    """
    visited = set()

    def dfs(box_num):
        if box_num in visited:
            return
        visited.add(box_num)

        for key in boxes[box_num]:
            dfs(key)

    dfs(0)

    return len(visited) == len(boxes)
