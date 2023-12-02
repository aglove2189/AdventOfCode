import math

from get_data import get_data

data = get_data(2023, 2).splitlines()

p1 = 0
p2 = 0
for i, game in enumerate(data, 1):
    valid = True
    maxes = {}
    _, game = game.split(":")
    for sets in game.split(";"):
        counts = {"red": 12, "green": 13, "blue": 14}
        for count, color in [i.strip().split() for i in sets.split(",")]:
            counts[color] -= int(count)
            maxes[color] = max(maxes.get(color, 0), int(count))
        if any(c < 0 for c in counts.values()):
            valid = False
    p1 += i if valid else 0
    p2 += math.prod(maxes.values())
print(p1)
print(p2)
