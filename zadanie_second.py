import numpy as np


def insert_columns(array, k, s, n_zeros):
    new_shape = array.shape + (n_zeros,)
    new_array = np.zeros(new_shape)

    for row in range(array.shape[0]):
        new_array[row, :array.shape[1]] = array[row, :]
        new_array[row, array.shape[1] + k] = array[row, s]
        new_array[row, array.shape[1] + s + 1 + n_zeros] = array[
            row, s + 1
        ]

    return new_array
