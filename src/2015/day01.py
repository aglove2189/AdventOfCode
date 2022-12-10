# -*- coding: utf-8 -*-
from collections import Counter

from get_data import get_data

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
