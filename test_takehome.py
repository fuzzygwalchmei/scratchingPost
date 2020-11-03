import pytest
import takehome
# Takehome test file



## Functional Arrays

# Create a function that takes a lambda, a dimensions shape and the Numpy dtype, and produces an array.


import numpy as np

def test_create_array_from_function():
    expected = np.array([[0, 1, 4, 9], [1, 0, 1, 4,], [4, 1, 0, 1],[9, 4, 1, 0]])
    actual = takehome.create_array_from_function(lambda i,j: (i - j)**2, [4, 4])
    assert expected == actual


## Removing Boundaries

# Create a function that takes an array and a binary mask and produces a cropped array based on the binary mask.

def test_boundary_cropping():
    expected_a1 = [[1, 0, 1, 1]]
    expected_a2 = [[[1], [1]], [[1], [0]], [[1], [0]]]
    a1 = np.array([[0,0,0,0,0], [0,0,0,0,0], [0,1,0,1,1], [0,0,0,0,0]])
    a2 = np.array([[ [0,0,0], [0,1,0], [0,1,0] ], [ [0,0,0], [0,1,0], [0,0,0] ], [ [0,0,0], [0,1,0], [0,0,0] ]])

    actual_a1 = takehome.boundary_cropping(a1, a1 != 0)
    actual_a2 = takehome.boundary_cropping(a2, a2 != 0)

    assert expected_a1 == actual_a1
    assert expected_a2 == actual_a2

    
## Block Reshaping

# Create a function that takes an 2D matrix, a number of rows and an number of columns which reshapes the 2D matrix into blocks of the rows and columns.

def test_shape_as_blocks():
    arr = np.array([[1,2,3,4], [5,6,7,8], [9,0,1,2]])
    actual = takehome.shape_as_blocks(arr, 2, 2)
    expected = array([[[[1, 2], [7, 8]], [[3, 4], [9, 0]], [[5, 6], [1, 2]]]])
    assert expected == actual


## Population Variance from Subpopulation Variance

# Given a list of numpy arrays, where each array is a subpopulation and the entire list is the population, calculate the variance of the entire population from the variance of the subpopulations.


def test_pop_var_from_subpop_var():
    groups = [np.array([1,2,3,4]), np.array([5,6])]
    actual = takehome.pop_var_from_subpop_var(groups)
    expected = 2.9166666666666665

    assert actual == expected


## Shuffle a Large List

#Given a very large list of numbers, randomly shuffle the list while using constant memory.

import random

l = [1,2,3,4,5]

def test_shuffle_list_inplace_constant_memory():
    pass

## Acquiring Coordinates

# Given an array and a step shape, return a list of coordinates based on each step.


import itertools
import numpy as np

def test_coordinates_from_steps():
    actual_1 = takehome.coordinates_from_steps(np.array([[1,2],[3,4]]), (1,1))
    expected_1 = [[0, 0],[0, 1], [1, 0], [1, 1]]

    actual_2 = takehome.coordinates_from_steps(np.array([[1,2],[3,4]]), (1,2))
    expected_2 = [[0, 0], [1, 0]]

    assert actual_1 == expected_1
    assert actual_2 == expected_2
