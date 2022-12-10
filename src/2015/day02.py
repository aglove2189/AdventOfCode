# -*- coding: utf-8 -*-
from get_data import get_data

data = get_data(2015, 2)

part1 = 0
part2 = 0
for d in data.split():
    l, w, h = d.split("x")
    l, w, h = int(l), int(w), int(h)

    sides = (2 * l * w, 2 * w * h, 2 * h * l)
    part1 += sum(sides) + (min(sides) / 2)

    s = sorted((l, w, h))
    part2 += s[0] + s[0] + s[1] + s[1] + (l * w * h)
print(part1)
print(part2)
