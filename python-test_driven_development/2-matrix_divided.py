#!/usr/bin/python3
""" matrix_divided divides the given matrix
by the parameter "div", and returns the divided matrix
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix by "div"
    checks if the entire list is int/float
    checks if each list in the matrix are the same size
    checks if "div" is an int/float or is 0
    """
    mes0 = "matrix must be a matrix (list of lists) of integers/floats"
    mes1 = "Each row of the matrix must have the same size"

    # Check if div is a number (but not bool, since bool is a subclass of int)
    if isinstance(div, bool) or not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError(mes0)

    # Check if matrix is empty
    if len(matrix) == 0:
        raise TypeError(mes0)

    res_matrix = []
    first_row_len = None

    for lists in matrix:
        # Check if each element is a list (not tuple or other)
        if not isinstance(lists, list):
            raise TypeError(mes0)

        # Check if row is empty
        if len(lists) == 0:
            raise TypeError(mes0)

        # Set the first row length as reference
        if first_row_len is None:
            first_row_len = len(lists)

        # Check if each row has the same size
        if len(lists) != first_row_len:
            raise TypeError(mes1)

        inner_list = []
        for items in lists:
            # Check if item is a number (but not bool)
            if isinstance(items, bool) or not isinstance(items, (int, float)):
                raise TypeError(mes0)
            inner_list.append(round(items / div, 2))
        res_matrix.append(inner_list)

    return res_matrix
