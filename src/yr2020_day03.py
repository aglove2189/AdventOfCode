# -*- coding: utf-8 -*-
from get_data import get_data


data = get_data(2020, 3).splitlines()


def count_trees(data, right=3, down=1):
    trees = 0
    pos = 1
    for i in range(0, len(data), down):
        d = data[i]
        trees += d[pos-1] == '#'
        pos += right
        if pos > len(d):
            pos -= len(d)
    return trees


print(count_trees(data))
print(
      count_trees(data, 1, 1)
      * count_trees(data, 3, 1)
      * count_trees(data, 5, 1)
      * count_trees(data, 7, 1)
      * count_trees(data, 1, 2)
)
