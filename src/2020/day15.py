# -*- coding: utf-8 -*-
from get_data import get_data

data = list(map(int, get_data(2020, 15).split(',')))

for num in (2020, 30000000):
    seen, last = {e: i for i, e in enumerate(data, 1)}, data[-1]
    for i in range(len(data), num):
        seen[last], last = i, 0 if last not in seen else i-seen[last]
    print(last)
