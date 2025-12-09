from get_data import get_data
from shapely.geometry import Polygon, box

data = get_data(2025, 9).split()
points = [tuple(map(int, d.split(","))) for d in data]

part1 = 0
part2 = 0
poly = Polygon(points)

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]

        minx, maxx = min(x1, x2), max(x1, x2)
        miny, maxy = min(y1, y2), max(y1, y2)

        area = (maxx - minx + 1) * (maxy - miny + 1)

        if area > part1:
            part1 = area

        rect = box(minx, miny, maxx, maxy)
        if area > part2 and poly.covers(rect):
            part2 = area

print(part1)
print(part2)
