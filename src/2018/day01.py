# -*- coding: utf-8 -*-
from get_data import get_data

data = get_data(2018, 1)

count = 0
for r in data.split():
    count += int(r)
print(count)

count = 0
c = set()
run = True
while run:
    for r in data.split():
        count += int(r)
        orig_len = len(c)
        c.add(count)
        if orig_len == len(c):
            print(count)
            run = False
            break
