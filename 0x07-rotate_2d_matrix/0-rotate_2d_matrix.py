#!/usr/bin/python3
"""
rotate 2d matrix
"""


def rotate_2d_matrix(matrix):
    """
    rotate a 2d matrix 90 degrees clockwise

    Args:
        matrix: this has to be a 2d matrix in list form

    Return:
        a 90 degrees rotated matrix in list form
    """
    length_of_matrix = len(matrix)
    rotated_2d_matrix = [[] for i in range(0, length_of_matrix)]
    for i in range(len(matrix) - 1, -1, -1):
        index = 0
        for j in rotated_2d_matrix:
            j.append(matrix[i][index])
            index += 1
    for x in range(len(matrix)):
        matrix[x] = rotated_2d_matrix[x]
