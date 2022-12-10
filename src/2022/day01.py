# -*- coding: utf-8 -*-
from get_data import get_data

data = get_data(2022, 1)

calories_per_elf = [sum(list(map(int, i.split()))) for i in data.split('\n\n')]

print(max(calories_per_elf))
print(sum(sorted(calories_per_elf)[-3:]))
