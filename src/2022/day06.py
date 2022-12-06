# -*- coding: utf-8 -*-
from get_data import get_data


data = get_data(2022, 6)


def solve(n=4):
    for i in range(n, len(data)):
        if len(set(data[i-n:i])) == n:
            return i


print(solve())
print(solve(14))
