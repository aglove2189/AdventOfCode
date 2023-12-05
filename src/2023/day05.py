from functools import reduce

from get_data import get_data

data = get_data(2023, 5)

seeds, *maps = data.split("\n\n")
seeds = map(int, seeds.split()[1:])


def seed_to_location(cur, maps):
    _, *ranges = maps.split("\n")
    for r in ranges:
        dst, src, n = map(int, r.split())
        if src <= cur < src + n:
            return cur - src + dst
    else:
        return cur


print(min(reduce(seed_to_location, maps, s) for s in seeds))
