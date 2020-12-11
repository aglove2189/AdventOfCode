# -*- coding: utf-8 -*-
import itertools
import copy
from get_data import get_data


data = get_data(2020, 11)
deltas = [[1, 0], [-1, 0], [0, -1], [0, 1], [1, 1], [-1, -1], [1, -1], [-1, 1]]


def next_grid(grid):
    new_grid = copy.deepcopy(grid)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            adjacent = []
            for i, j in deltas:
                if 0 <= row + i < len(grid) and 0 <= col + j < len(grid[0]):
                    adjacent.append(grid[row+i][col+j])
            if grid[row][col] == "L" and "#" not in adjacent:
                new_grid[row][col] = "#"
            if grid[row][col] == "#" and adjacent.count("#") >= 4:
                new_grid[row][col] = "L"
    return new_grid


def next_grid2(grid):
    new_grid = copy.deepcopy(grid)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            adjacent = []
            for i, j in deltas:
                step = 1
                while 0 <= row+step*i < len(grid) and 0 <= col+step*j < len(grid[0]):
                    changes = grid[row+step*i][col+step*j]
                    if changes != ".":
                        adjacent.append(changes)
                        break
                    step += 1
            if grid[row][col] == "L" and "#" not in adjacent:
                new_grid[row][col] = "#"
            if grid[row][col] == "#" and adjacent.count("#") > 4:
                new_grid[row][col] = "L"
    return new_grid


for grid_func in (next_grid, next_grid2):
    grid = [list(d) for d in data.splitlines()]
    new_grid = grid_func(grid)
    while new_grid != grid:
        grid, new_grid = new_grid, grid_func(new_grid)
    print(list(itertools.chain.from_iterable(grid)).count("#"))
