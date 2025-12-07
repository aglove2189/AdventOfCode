from collections import Counter
from get_data import get_data

data = get_data(2025, 7).split()

beams = Counter({data[0].index("S"): 1})

part1 = 0

for d in data[1:]:
    next_beams = Counter()

    for x, count in beams.items():
        if d[x] == "^":
            part1 += 1
            if x - 1 >= 0:
                next_beams[x - 1] += count
            if x + 1 < len(data[0]):
                next_beams[x + 1] += count
        else:
            next_beams[x] += count

    beams = next_beams

print(part1)
print(sum(beams.values()))
