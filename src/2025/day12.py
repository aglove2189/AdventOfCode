from get_data import get_data

data = get_data(2025, 12)

*shapes, regions = data.split("\n\n")
shapes = [s.count("#") for s in shapes]

part1 = 0
for region in regions.split("\n"):
    region, amts = region.split(": ")
    w, h = map(int, region.split("x"))
    amts = map(int, amts.split())
    area = sum(a * s for a, s in zip(amts, shapes))
    part1 += area <= w * h
print(part1)
