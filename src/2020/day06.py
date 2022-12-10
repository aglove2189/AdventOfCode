from collections import Counter

from get_data import get_data

data = get_data(2020, 6).split("\n\n")

print(sum(len(set(d.replace("\n", ""))) for d in data))
print(sum(len([k for k in Counter(d) if Counter(d)[k] == len(d.split())]) for d in data))
