# -*- coding: utf-8 -*-
from get_data import get_data


data = get_data(2020, 2)

part1 = 0
part2 = 0
for d in data.splitlines():
    policy, password = d.split(':')
    password = password.strip()

    min_, max_ = policy.split('-')
    max_ = "".join(filter(str.isdigit, max_))
    min_ = int(min_)
    max_ = int(max_)

    if min_ <= password.count(policy[-1]) <= max_:
        part1 += 1

    if (policy[-1] == password[min_-1]) != (policy[-1] == password[max_-1]):
        part2 += 1

print(part1)
print(part2)
