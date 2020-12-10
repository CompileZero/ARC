#!/usr/bin/python

import os
import sys
import json
import numpy as np
import re
import copy

# Atharva Kulkarni
# 20231773
# GitHub Link: https://github.com/CompileZero/ARC
# YOUR CODE HERE: write at least three functions which solve
# specific tasks by transforming the input x and returning the
# result. Name them according to the task ID as in the three
# examples below. Delete the three examples. The tasks you choose
# must be in the data/training directory, not data/evaluation.


def solve_dc1df850(x):
    x1 = copy.deepcopy(x)
    red, blue = 2, 1

    Dy = [-1, 0, 1, 0]
    Dx = [0, -1, 0, 1]
    for i in range(len(x1)):
        for j in range(len(x1[0])):
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
    return type(x1)


def solve_93b581b8(x):
    x2 = copy.deepcopy(x)
    for i in range(len(x2)):
        for j in range(len(x2[0])):
            if x2[i, j] != 0:
                print("Hello")
    return x2


def solve_3bd67248(x):
    x3 = copy.deepcopy(x)
    red, yellow = 2, 4
    for i in range(1, len(x3[0])):
        x3[len(x3) - 1, i] = yellow
        x3[len(x3) - 1 - i, i] = red
    print(x3)
    return x3


def solve_952a094c(x):
    x4 = copy.deepcopy(x)
    print(get_closed_area(x4))
    print("Hello")
    return x4


def get_closed_area(arr):
    # depth first search
    green = 3
    H, W = arr.shape
    Dy = [0, -1, 0, 1]
    Dx = [1, 0, -1, 0]
    arr_padded = np.pad(arr, ((1, 1), (1, 1)), "constant", constant_values=0)
    searched = np.zeros(arr_padded.shape, dtype=bool)
    searched[0, 0] = True
    q = [(0, 0)]
    while q:
        y, x = q.pop()
        for dy, dx in zip(Dy, Dx):
            y_, x_ = y+dy, x+dx
            if not 0 <= y_ < H+2 or not 0 <= x_ < W+2:
                continue
            if not searched[y_][x_] and arr_padded[y_][x_] == 0:
                q.append((y_, x_))
                searched[y_, x_] = True
    res = searched[1:-1, 1:-1]
    res |= arr == green
    return ~res


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
