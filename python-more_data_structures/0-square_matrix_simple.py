#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    matrixcopy = matrix.copy()

    for idx in range(len(matrix)):
        matrixcopy[idx] = list(map(lambda x: x**2, matrix[idx]))
    return (matrixcopy)
