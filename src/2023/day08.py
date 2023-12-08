from collections import namedtuple
import math

from get_data import get_data

data = get_data(2023, 8).splitlines()

lr = namedtuple("lr", "L R")
network = {d[0:3]: lr(d[7:10], d[12:15]) for d in data[2:]}


def solve(start="AAA"):
    steps = 0
    while start != "ZZZ" if start == "AAA" else not start.endswith("Z"):
        for direction in data[0]:
            steps += 1
            start = getattr(network[start], direction)
    return steps


print(solve())
print(math.lcm(*(solve(n) for n in network if n.endswith("A"))))
