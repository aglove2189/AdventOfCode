# -*- coding: utf-8 -*-
from get_data import get_data
from copy import deepcopy


data = get_data(2020, 8).splitlines()
instr = [d.split(' ') for d in data]


def run(instr, part1=True):
    acc = 0
    pos = 0
    seen = []
    while True:
        d = instr[pos]
        if 'acc' in d:
            acc += int(d[1])
            pos += 1
        elif 'nop' in d:
            pos += 1
        elif 'jmp' in d:
            pos += int(d[1])
        if pos in seen:
            if part1:
                return acc
            break
        if pos == len(instr):
            return acc
        seen.append(pos)


print(run(instr))

for i in range(len(instr)):
    instr_ = deepcopy(instr)
    if 'jmp' in instr_[i]:
        instr_[i][0] = 'nop'
    elif 'nop' in instr_[i]:
        instr_[i][0] = 'jmp'
    else:
        continue
    result = run(instr_, part1=False)
    if result:
        print(result)
        break
