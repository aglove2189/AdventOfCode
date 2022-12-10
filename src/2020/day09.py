from itertools import combinations

from get_data import get_data

data = list(map(int, get_data(2020, 9).splitlines()))

for i in range(25, len(data)):
    if data[i] not in map(sum, combinations(data[i - 25 : i], 2)):
        part1 = data[i]
        break
print(part1)

for i in range(len(data)):
    for j in range(i + 2, len(data)):
        s = data[i:j]
        if sum(s) == part1:
            part2 = min(s) + max(s)
            break
print(part2)
