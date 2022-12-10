# -*- coding: utf-8 -*-
from get_data import get_data

data = get_data(2020, 2)

part1 = 0
part2 = 0
for d in data.splitlines():
    min_max, char, password = d.split()
    min_, max_ = (int(i) for i in min_max.split("-"))

    part1 += min_ <= password.count(char[0]) <= max_
    part2 += (char[0] == password[min_ - 1]) != (char[0] == password[max_ - 1])
print(part1)
print(part2)
