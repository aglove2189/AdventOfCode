# -*- coding: utf-8 -*-
from get_data import get_data

import numpy as np 


data = get_data(2017, 3)

def pos(num):
    direction = -1
    count = 1
    x = 0
    y = 0
    i = 1
    while i <= num:
        for _ in range(count):
            i += 1
            x += direction
            if i == num:
                return x, y
        for _ in range(count):
            i += 1
            y += direction
            if i == num:
                return x, y
        direction *= -1
        count += 1

x, y = pos(eval(data))

print(abs(x) + abs(y))

# TODO part2
