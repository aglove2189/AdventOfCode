# -*- coding: utf-8 -*-
from string import ascii_letters

from get_data import get_data

data = get_data(2022, 3).split("\n")

part1 = 0
for rucksack in data:
    split = len(rucksack) // 2
    (letter,) = set(rucksack[split:]) & set(rucksack[:split])
    part1 += ascii_letters.find(letter) + 1
print(part1)

part2 = 0
for i in range(0, len(data), 3):
    (letter,) = set.intersection(*map(set, data[i:i + 3]))
    part2 += ascii_letters.find(letter) + 1
print(part2)
