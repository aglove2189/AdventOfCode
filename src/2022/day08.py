# -*- coding: utf-8 -*-
from get_data import get_data
import numpy as np


data = np.array([[int(i) for i in d] for d in get_data(2022, 8).splitlines()])

part1 = 0
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        height = data[i, j]
        if (
            np.all(data[:i, j] < height)
            or np.all(data[i, :j] < height)
            or np.all(data[i + 1 :, j] < height)
            or np.all(data[i, j + 1 :] < height)
        ):
            part1 += 1
print(part1)

part2 = 0
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        height = data[i, j]
        best = 1
        for arr in [data[:i, j][::-1], data[i, :j][::-1], data[i + 1 :, j], data[i, j + 1 :]]:
            score = 0
            for k in arr:
                score += 1
                if k >= height:
                    break
            best *= score
        part2 = max(part2, best)
print(part2)
