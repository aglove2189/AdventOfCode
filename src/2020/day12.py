# -*- coding: utf-8 -*-
from get_data import get_data

data = get_data(2020, 12).splitlines()

x, y = 0, 0
degrees = 90
for d in data:
    p, v = d[0], int(d[1::])
    if p == "F":
        if degrees % 360 == 0:
            p = "N"
        elif degrees % 360 == 90:
            p = "E"
        elif degrees % 360 == 180:
            p = "S"
        else:
            p = "W"
    if p == "N":
        y += v
    elif p == "S":
        y -= v
    elif p == "E":
        x += v
    elif p == "W":
        x -= v
    elif p == "L":
        degrees -= v
    else:
        degrees += v
print(abs(x) + abs(y))

x, y = 0, 0
wx, wy = 10, 1
for d in data:
    p, v = d[0], int(d[1::])
    if p == "F":
        x += wx * v
        y += wy * v
    if p == "N":
        wy += v
    elif p == "S":
        wy -= v
    elif p == "E":
        wx += v
    elif p == "W":
        wx -= v
    elif p == "L":
        for i in range(v // 90):
            wx, wy = -wy, wx
    elif p == "R":
        for i in range(v // 90):
            wx, wy = wy, -wx
print(abs(x) + abs(y))
