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

        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        part1 = max(area, part1)

        if area > part2:
            rect = box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
            if poly.covers(rect):
                part2 = area

print(part1)
print(part2)
