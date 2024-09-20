#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    i = 0
    new_matrix = [sub[:] for sub in matrix]

    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            new_matrix[i][j] = matrix[i][j] ** 2
            j += 1
        i += 1
    return new_matrix
