# -*- coding: utf-8 -*-
import re

from get_data import get_data

data = get_data(2015, 5)


def has_bad(data):
    return any(x in data for x in ("ab", "cd", "pq", "xy"))


def has_vowels(data):
    return sum(1 for x in data if x in "aeiou") >= 3


def has_same(data):
    return any(x[0] == x[1] for x in zip(data, data[1:]))


count = 0
for d in data.split():
    if has_vowels(d) and not has_bad(d) and has_same(d):
        count += 1
print(count)

count = 0
for d in data.split("\n"):
    dup = re.search(r"(..).*\1", d)
    between = re.search(r"(.).\1", d)
    if dup and between:
        count += 1
print(count)
