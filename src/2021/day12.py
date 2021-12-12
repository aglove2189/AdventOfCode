# -*- coding: utf-8 -*-
from get_data import get_data
from collections import defaultdict

data = get_data(2021, 12).splitlines()

C = defaultdict(list)
for d in data:
    a, b = d.split('-')
    C[a].append(b)
    C[b].append(a)


def get_paths(cave="start", seen=set()):
    if cave == 'end':
        return 1
    if cave.islower() and cave in seen:
        return 0
    seen = seen | {cave}
    paths = 0
    for cave in C[cave]:
        paths += get_paths(cave, seen)
    return paths


def get_paths2(cave="start", seen=set(), twice=None):
    if cave == 'end':
        return 1
    if cave == 'start' and seen:
        return 0
    if cave.islower() and cave in seen:
        if twice is None:
            twice = cave
        else:
            return 0
    seen = seen | {cave}
    paths = 0
    for cave in C[cave]:
        paths += get_paths2(cave, seen, twice)
    return paths


print(get_paths())
print(get_paths2())
