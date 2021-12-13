# -*- coding: utf-8 -*-
from get_data import get_data
from parse import findall


data = get_data(2021, 13)
dots = findall("{:d},{:d}", data)
folds = findall("{:l}={:d}", data)

for i, (axis, line) in enumerate(folds):
    if axis == "x":
        dots = {(min(x, 2 * line - x), y) for x, y in dots}
    else:
        dots = {(x, min(y, 2 * line - y)) for x, y in dots}
    print(len(dots)) if i == 0 else None


x_max, y_max = map(max, zip(*dots))
for y in range(y_max + 1):
    print(*[" #"[(x, y) in dots] for x in range(x_max + 1)])
