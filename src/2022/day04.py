# -*- coding: utf-8 -*-
import re

from get_data import get_data

data = get_data(2022, 4).split("\n")

part1 = 0
part2 = 0
for i in data:
    min1, max1, min2, max2 = list(map(int, re.findall(r"\d+", i)))

    if min1 >= min2 and max1 <= max2:
        part1 += 1
    elif min2 >= min1 and max2 <= max1:
        part1 += 1

    if set(range(min1, max1 + 1)) & set(range(min2, max2 + 1)):
        part2 += 1
print(part1)
print(part2)
