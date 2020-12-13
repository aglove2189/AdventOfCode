# -*- coding: utf-8 -*-
import math
import itertools
from get_data import get_data


timestamp, bus_ids = get_data(2020, 13).splitlines()
bus_ids = bus_ids.split(',')

bus_ids_no_x = [int(i) for i in bus_ids if i != 'x']
part1 = min([(math.ceil(int(timestamp) / i) * i, i) for i in bus_ids_no_x])
print((part1[0] - int(timestamp)) * part1[1])

n, step = int(bus_ids[0]), 1
for i, bus_id in enumerate(bus_ids):
    if bus_id == 'x':
        continue
    n = next(c for c in itertools.count(n, step) if (c + i) % int(bus_id) == 0)
    step *= int(bus_id)
print(n)
