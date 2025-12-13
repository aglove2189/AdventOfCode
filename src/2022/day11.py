from copy import deepcopy
from math import prod
from get_data import get_data

data = get_data(2022, 11).split("\n\n")
items_init = []
ops = []
tests = []
paths = []

for d in data:
    d = d.split("\n")
    _, nums = d[1].split(": ")
    items_init.append(list(map(int, nums.split(","))))
    ops.append(d[2].split("= ")[1])
    tests.append(int(d[3][-2:].strip()))
    paths.append((int(d[5][-1]), int(d[4][-1])))

modulo = prod(tests)


def solve(rounds=20, is_part2=False):
    items = deepcopy(items_init)

    counts = [0] * len(items)

    for _ in range(rounds):
        for i in range(len(items)):
            while items[i]:
                counts[i] += 1
                old = items[i].pop(0)  # noqa: F841
                new = eval(ops[i])
                if is_part2:
                    new %= modulo
                else:
                    new //= 3
                condition = new % tests[i] == 0
                next_monkey = paths[i][condition]
                items[next_monkey].append(new)

    return prod(sorted(counts)[-2:])


print(solve())
print(solve(10_000, True))
