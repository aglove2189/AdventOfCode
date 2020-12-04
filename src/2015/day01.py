# -*- coding: utf-8 -*-
from get_data import get_data

from collections import Counter


data = get_data(2015, 1)

c = Counter(data)
print(c['('] - c[')'])

pos = 0
for index, d in enumerate(data):
    if pos == -1:
        print(index)
        break
    if d == '(':
        pos += 1
    if d == ')':
        pos -= 1
