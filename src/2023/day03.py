import math
import re

from get_data import get_data

data = get_data(2023, 3).split()

deltas = [[1, 0], [-1, 0], [0, -1], [0, 1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
gears = {(y, x): set() for y in range(len(data)) for x in range(len(data[y])) if data[y][x] == "*"}

p1 = 0
for y, d in enumerate(data):
    for match in re.finditer(r"\d+", d):
        num = int(match.group(0))
        adjacents = []
        for x in range(match.start(), match.end()):
            for dx, dy in deltas:
                try:
                    adjacents.append(data[dy + y][dx + x])
                    gears[(dy + y, dx + x)].add(num)
                except (IndexError, KeyError):
                    continue
        if any(a for a in adjacents if a not in "0123456789."):
            p1 += num

print(p1)
print(sum(math.prod(i) for i in gears.values() if len(i) == 2))
