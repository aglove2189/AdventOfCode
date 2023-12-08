from collections import namedtuple
import math

from get_data import get_data

data = get_data(2023, 8).splitlines()

lr = namedtuple("lr", "L R")
network = {d[0:3]: lr(d[7:10], d[12:15]) for d in data[2:]}

p1 = 0
current = "AAA"
while current != "ZZZ":
    for direction in data[0]:
        p1 += 1
        current = getattr(network[current], direction)
print(p1)

p2 = []
for current in network:
    if current.endswith("A"):
        steps = 0
        while not current.endswith("Z"):
            for direction in data[0]:
                steps += 1
                current = getattr(network[current], direction)
        p2.append(steps)
print(math.lcm(*p2))
