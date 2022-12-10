# -*- coding: utf-8 -*-
import numpy as np
from get_data import get_data

data = get_data(2021, 5).splitlines()


def overlap(data, include_diagonal=False):
    diagram = np.zeros((1000, 1000))
    for d in data:
        one, two = d.split(" -> ")
        x1, y1 = list(map(int, one.split(",")))
        x2, y2 = list(map(int, two.split(",")))
        if x1 == x2:
            diagram[x1, min(y1, y2):max(y1, y2) + 1] += 1
        elif y1 == y2:
            diagram[min(x1, x2):max(x1, x2) + 1, y1] += 1
        elif include_diagonal:
            xpoints = np.arange(x1, x2 + np.sign(x2 - x1), np.sign(x2 - x1))
            ypoints = np.arange(y1, y2 + np.sign(y2 - y1), np.sign(y2 - y1))
            diagram[xpoints, ypoints] += 1
    return np.sum(diagram >= 2)


print(overlap(data))
print(overlap(data, include_diagonal=True))
