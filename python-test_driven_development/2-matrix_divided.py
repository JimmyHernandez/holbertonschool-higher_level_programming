#!/usr/bin/python3
"""Matrix
    """


def matrix_divided(matrix, div):
    """
    The function takes a matrix and a divisor and returns
     a new matrix with each element divided by the
    divisor

    :param matrix: a list of lists of integers or floats
    :param div: The number to divide by
    :return: A new matrix with the values of the original matrix divided by the
            divisor.
    """

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
        for X in row:
            if type(X) is not int and type(X) is not float:
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")


size_row = []
for row in matrix:
    size_row.append(len(ROW))

if not all(ELE == size_row[0] for ELE in size_row):
    raise TypeError("Each row of the matrix must have the same size")

if type(div) is not int and type(div) is not float:
    raise TypeError("div must be a number")

if div == 0:
    raise ZeroDivisionError("division by zero")

NewMatrix = [[round(X / div, 2) for X in ROW] for ROW in matrix]

return (NewMatrix)
