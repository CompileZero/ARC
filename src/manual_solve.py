#!/usr/bin/python

import os
import sys
import json
import numpy as np
import re
import copy

"""
Name:- Atharva Kulkarni
Student ID:- 20231773
GitHub Link: https://github.com/CompileZero/ARC


Summary/Reflection:

The Multi-dimensional array problems from ARC were solved using pure python. The solutions have been written using a structural (procedural) programming approach and no machine learning or AI technique was used. Throughout the code, you can see the use of nested loops to traverse all elements of the array and perform the necessary operations on them. A new array is used to store and/or perform the operations and is returned by the function. 

The 'copy' module is used to create a deepcopy of the input array to avoid operating on the same array. 2 Utility functions from the 'Numpy' module are used - np.zeros to create an array of 0's and np.full to fill the entire array with a particular value. Accessing of an element from the array is done using 'Arr[i, j]' instead of the typically used 'Arr[i][j]', as the former is significantly faster when dealing with huge multi-dimensional arrays.
"""


# From the bottom-most row and 2nd column from the left, add a horizontal yellow line and a diagonal red line to the top-right point of the matrix
# Results: All training and testing Grids are solved correctly
def solve_3bd67248(x):
    red, yellow = 2, 4
    # Use deepcopy to avoid referencing to the same array
    x3 = copy.deepcopy(x)
    for i in range(1, len(x3[0])):
        # Append yellow for every position after the first position at the bottom-most row
        x3[len(x3) - 1, i] = yellow
        # Append red for diagonal positions till the top-right corner
        x3[len(x3) - 1 - i, i] = red
    return x3


# Given 2 3x3 matrices joined together by a gray line, find out the common blue squares between the 2 matrices and append them as red squares in a new 3x3 matrice
# Results: All training and testing Grids are solved correctly
def solve_0520fde7(x):
    red, blue = 2, 1
    x5 = np.zeros((3, 3), dtype=int)  # Create a 3x3 np.array of zeros
    for i in range(len(x)):
        for j in range(0, 3):
            # If the element at j matches the element at j+4 and is blue, then append red to the above create np.array at i, j position
            if x[i, j] == x[i, j+4] == blue:
                x5[i, j] = red
    return x5


# Given a 3x3 matrix, check for 3 occurences of a color and return a new matrix filled completely with that color
# Results: All training and testing Grids are solved correctly
def solve_5582e5ca(x):
    # Create an empty dictionary of keys: 0-9 with values 0, to store each color code as a key and number of occurences as its value
    count = {el: 0 for el in range(10)}
    for i in range(len(x)):
        for j in range(len(x[0])):
            count[x[i, j]] += 1
    # Get the key at which the value is 3
    most_frequent_color = list(count.keys())[list(count.values()).index(3)]
    # Return an np.array filled with the above retrieved color
    return np.full((3, 3), most_frequent_color)


# Given a matrix, search all the red squares and added a blue border of 1 square thickness around the red square. Check for border conditions as well
# Results: All training and testing Grids are solved correctly
def solve_dc1df850(x):
    red, blue = 2, 1
    # Use deepcopy to avoid referencing to the same array
    x1 = copy.deepcopy(x)
    for i in range(len(x1)):
        for j in range(len(x1[0])):
            # Check boundary conditions, if satisfied, then append a blue color at that position
            if x1[i, j] == red:
                if j+1 < len(x1[0]):
                    x1[i, j+1] = blue
                if j-1 >= 0:
                    x1[i, j-1] = blue
                if i+1 < len(x1):
                    x1[i+1, j] = blue
                if i-1 >= 0:
                    x1[i-1, j] = blue
                if i-1 >= 0 and j-1 >= 0:
                    x1[i-1, j-1] = blue
                if i+1 < len(x1) and j+1 < len(x1[0]):
                    x1[i+1, j+1] = blue
                if i-1 >= 0 and j+1 < len(x1[0]):
                    x1[i-1, j+1] = blue
                if j-1 >= 0 and i+1 < len(x1):
                    x1[i+1, j-1] = blue
    return x1


# Given a matrix of m rows and n columns, return a matrix of the same shape with dark blue coloured zig-zag lines along the matrix
# Results: All training and testing Grids are solved correctly
def solve_e179c5f4(x):
    blue, cyan = 1, 8
    # Create an array of the shape of the input and append cyan color at all positions
    x6 = np.full(x.shape, cyan)
    # This list stores the value of counts 0 to 3, and number of diagonal lines printed
    count_iter = [0, 0]
    for i in range(len(x6)-1, -1, -1):
        x6[i, count_iter[0]] = blue
        # If the next diagonal line is at an even position (0, 2, 4 etc), append diagonal elements from left to right
        if(count_iter[1] % 2 == 0):
            count_iter[0] += 1
        # If the next diagonal line is at an odd position (1, 3, 5 etc), append diagonal elements from right to left
        else:
            count_iter[0] -= 1
        # If count reaches the end or start of a row, increase the value of the number of diagonal lines printed
        if(count_iter[0] == len(x6[0]) - 1 or count_iter[0] == 0):
            count_iter[1] += 1
    return x6


def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})"
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals():
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1)  # just the task ID
            solve_fn = globals()[name]  # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join(".", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    data = read_ARC_JSON("data/training/dc1df850.json")
    # print(data)
    # test("dc1df850", solve_dc1df850, data)
    # solve_dc1df850()


def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""

    # Open the JSON file and load it
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input'])
                   for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output'])
                    for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input'])
                  for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output'])
                   for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)


def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    # if yhat has the right shape, then (y == yhat) is a bool array
    # and we test whether it is True everywhere. if yhat has the wrong
    # shape, then y == yhat is just a single bool.
    print(np.all(y == yhat))


if __name__ == "__main__":
    main()
