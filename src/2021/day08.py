# -*- coding: utf-8 -*-
from get_data import get_data

data = get_data(2021, 8).splitlines()
data = [d.split(' | ') for d in data]

part1 = []
for _, output in data:
    part1.extend([i for i in list(map(len, output.split())) if i in [2, 4, 3, 7]])
print(len(part1))
