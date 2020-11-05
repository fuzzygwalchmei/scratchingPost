
'''
 Author: Marc Falzon (marc.falzon@gmail.com)
 Takehome
 Hi prospective Junior Data Engineer! Here is your assignment. 
 You are allowed to use the Python standard library and basic utilities from Numpy. Points are given for **succinct**
 but __clear__ code, and when there are ambiguities, comments should be provided. Using functional programming style 
 is allowed. For Python, using the pep8 standard is encouraged. The challenges below will give you a few correct inputs
 and outputs, however we will be testing your functions against unseen inputs. So make sure you understand exactly the 
 purpose of the function.
 All code is to be submitted that works against Python 3 and a current version of Numpy.
 Submit the code as separate `takehome.py` file.
# Functional Arrays

# Create a function that takes a lambda, a dimensions shape and the Numpy dtype, and produces an array.
'''

import numpy as np

def create_array_from_function(f, d, dtype=None):
    return np.array([[f(i,j) for j in range(1, d[1]+1)]for i in range(1, d[0]+1)], dtype=dtype)

'''   
# print(create_array_from_function(lambda i,j: (i - j)**2, [4, 4]))
# [[0. 1. 4. 9.]
#  [1. 0. 1. 4.]
#  [4. 1. 0. 1.]
#  [9. 4. 1. 0.]]

## Removing Boundaries

# Create a function that takes an array and a binary mask and produces a cropped array based on the binary mask.
'''

import numpy as np

def boundary_cropping(a, m):
    valid_coords = np.argwhere(m)
    begin_coords = valid_coords.min(axis = 0)
    finish_coords = valid_coords.max(axis = 0) + 1
    array_slice = tuple(slice(start, end) for (start, end) in zip(begin_coords, finish_coords))
    return a[array_slice]


# a1 = np.array([[0,0,0,0,0], [0,0,0,0,0], [0,1,0,1,1], [0,0,0,0,0]])
# a2 = np.array([[ [0,0,0], [0,1,0], [0,1,0] ], [ [0,0,0], [0,1,0], [0,0,0] ], [ [0,0,0], [0,1,0], [0,0,0] ]])

# print(boundary_cropping(a1, a1 != 0))
# # [[1 0 1 1]]
# print(boundary_cropping(a2, a2 != 0))
# # [[[1] [1]] [[1] [0]] [[1] [0]]]

## Block Reshaping

# Create a function that takes an 2D matrix, a number of rows and an number of columns which reshapes the 2D matrix into blocks of the rows and columns.

import numpy as np

def shape_as_blocks(a, r, c):
    return np.array([a.reshape(r,-1, c).swapaxes(0,1)])

# arr = np.array([[1,2,3,4], [5,6,7,8], [9,0,1,2]])
# print(shape_as_blocks(arr, 2, 2))
# array([[[[1, 2],
#          [7, 8]],
# 
#         [[3, 4],
#          [9, 0]],
# 
#         [[5, 6],
#          [1, 2]]]])


## Population Variance from Subpopulation Variance

# Given a list of numpy arrays, where each array is a subpopulation and the entire list is the population, calculate the variance of the entire population from the variance of the subpopulations.

import numpy as np

def pop_var_from_subpop_var(groups):
    t_pop = [x for y in groups for x in y]
    t_mean = sum(t_pop)/len(t_pop)

    sub_p_var = [(i-t_mean)**2 for i in t_pop]
    return sum(sub_p_var)/len(sub_p_var)

    
#groups = [np.array([1,2,3,4]), np.array([5,6])]
#print(pop_var_from_subpop_var(groups))
# 2.9166666666666665


## Shuffle a Large List

# Given a very large list of numbers, randomly shuffle the list while using constant memory.


import random

# l = [1,2,3,4,5]

def shuffle_list_inplace_constant_memory(l):
    for i in range(len(l)-1, 0, -1):
        x = random.randrange(i+1)
        l[i], l[x] = l[x], l[i]
    return l


## Acquiring Coordinates

# Given an array and a step shape, return a list of coordinates based on each step.


import itertools
import numpy as np

def coordinates_from_steps(a, s, dtype=int):
    pass

