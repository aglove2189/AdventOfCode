# -*- coding: utf-8 -*-
import numpy as np
from get_data import get_data

data = get_data(2021, 11).splitlines()
data = np.array([[int(y) for y in x] for x in data])

part1, part2 = 0, 0
while True:
    part2 += 1
    data += 1
    flashing = np.where((data > 9) & (data < 420))
    while len(flashing[0]) > 0:
        for x, y in list(zip(*flashing)):
            data[
                max(0, x - 1) : min(x + 2, data.shape[0]), max(0, y - 1) : min(y + 2, data.shape[1])
            ] += 1
            data[x, y] += 420
            part1 += 1 if part2 <= 100 else 0
        flashing = np.where((data > 9) & (data < 420))
    data[data > 420] = 0
    if data.sum() == 0:
        print(part1, part2)
        break
