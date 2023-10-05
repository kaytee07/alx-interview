#!/usr/bin/python3
"""
unlock all boxes with available keys
"""


def canUnlockAll(boxes):
    """
    unlock all boxes
    """
    if not boxes:
        return False

    num_of_boxes = len(boxes)
    visited = set()

    def dfs(box_num):
        if box_num in visited:
            return
        visited.add(box_num)

        for key in boxes[box_num]:
            if key < num_of_boxes:
                dfs(key)

    dfs(0)

    return len(visited) == len(boxes)
