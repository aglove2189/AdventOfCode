from get_data import get_data
from itertools import groupby
from math import prod

data = get_data(2025, 6).splitlines()

nums = [map(int, d.split()) for d in data[:-1]]
ops = data[-1].split()

part1 = 0
for *nums, op in zip(*nums, ops):
    part1 += sum(nums) if op == "+" else prod(nums)
print(part1)

data = list(zip(*data))

part2 = 0
for is_sep, group in groupby(data, key=lambda row: all(c == " " for c in row)):
    if not is_sep:
        nums = []
        op = None
        for col in group:
            nums.append(int("".join(c for c in col if c.isdigit())))
            if "+" in col:
                op = "+"
            if "*" in col:
                op = "*"
        part2 += sum(nums) if op == "+" else prod(nums)
print(part2)
