# -*- coding: utf-8 -*-
import itertools
from collections import Counter

from get_data import get_data
from nltk.metrics import edit_distance

data = get_data(2018, 2)

dub = 0
trip = 0
for r in data.split():
    A = Counter(r)
    if 2 in A.values():
        dub += 1
    if 3 in A.values():
        trip += 1
print(dub * trip)

for f, s in itertools.permutations(data.split(), 2):
    if edit_distance(f, s) == 1:
        print(f, s)
        break
