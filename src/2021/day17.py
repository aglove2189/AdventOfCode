# -*- coding: utf-8 -*-
from get_data import get_data


print(get_data(2021, 17))
x1, x2, y1, y2 = 201, 230, -99, -65
print(y1 * (y1 + 1) // 2)


def sim(x, y, xpos=0, ypos=0):
    if xpos > x2 or ypos < y1:
        return 0
    if xpos >= x1 and ypos <= y2:
        return 1
    return sim(x - (x > 0), y - 1, xpos + x, ypos + y)


hits = [sim(x, y) for x in range(1, x2 + 1) for y in range(y1, abs(y1))]
print(sum(hits))
