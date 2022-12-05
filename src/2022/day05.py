# -*- coding: utf-8 -*-
from get_data import get_data
import re
import copy


stacks, instructions = data = get_data(2022, 5).split("\n\n")

stacks = [
    list("PFMQWGRT"),
    list("HFR"),
    list("PZRVGHSD"),
    list("QHPBFWG"),
    list("PSMJH"),
    list("MZTHSRPL"),
    list("PTHNML"),
    list("FDQR"),
    list("DSCNLPH"),
]


def solve(stacks, part1=True):
    stacks_c = copy.deepcopy(stacks)
    for i in instructions.splitlines():
        a, b, c = map(int, re.findall(r"\d+", i))
        if part1:
            for _ in range(a):
                stacks_c[c-1].append(stacks_c[b-1].pop())
        else:
            stacks_c[c-1] += stacks_c[b-1][-a:]
            stacks_c[b-1] = stacks_c[b-1][:-a]
    return "".join(i[-1] for i in stacks_c)


print(solve(stacks))
print(solve(stacks, part1=False))
