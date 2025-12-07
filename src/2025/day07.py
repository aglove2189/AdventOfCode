from collections import Counter
from get_data import get_data

data = get_data(2025, 7).split()

beams = Counter({data[0].index("S"): 1})

part1 = 0
part2 = 0

for d in data[1:]:
    next_beams = Counter()

    for x, count in beams.items():
        if d[x] == "^":
            part1 += 1
            targets = [x - 1, x + 1]
        else:
            targets = [x]

        for t in targets:
            if 0 <= t < len(data[0]):
                next_beams[t] += count
            else:
                part2 += count

    beams = next_beams

part2 += sum(beams.values())

print(part1)
print(part2)
