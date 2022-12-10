# -*- coding: utf-8 -*-
from get_data import get_data

data = get_data(2019, 1)


def fuel(mass):
    return int(mass) // 3 - 2


print(sum([fuel(d) for d in data.split()]))


def fuel_total(mass):
    f = fuel(mass)
    return f + fuel_total(f) if f > 0 else 0


print(sum([fuel_total(d) for d in data.split()]))
