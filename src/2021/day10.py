# -*- coding: utf-8 -*-
from get_data import get_data

data = get_data(2021, 10).splitlines()

matches = {')': '(', '}': '{', ']': '[', '>': '<'}
points_pt1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
points_pt2 = {'(': 1, '[': 2, '{': 3, '<': 4}

part1 = 0
part2 = []
for d in data:
    stack = []
    for char in list(d.strip()):
        if char in matches.values():
            stack.append(char)
        elif not stack or stack.pop() != matches[char]:
            part1 += points_pt1[char]
            stack = None
            break

    if stack:
        subtotal = 0
        for char in stack[::-1]:
            subtotal = 5 * subtotal + points_pt2[char]
        part2.append(subtotal)

print(part1)
print(sorted(part2)[len(part2) // 2])
