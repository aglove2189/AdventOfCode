# -*- coding: utf-8 -*-
from get_data import get_data


data = get_data(2021, 9).splitlines()
data = [[int(y) for y in x] for x in data]

part1 = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if i > 0 and data[i][j] >= data[i - 1][j]:
            continue
        if i < len(data) - 1 and data[i][j] >= data[i + 1][j]:
            continue
        if j > 0 and data[i][j] >= data[i][j - 1]:
            continue
        if j < len(data[0]) - 1 and data[i][j] >= data[i][j + 1]:
            continue
        part1 += data[i][j] + 1
print(part1)
