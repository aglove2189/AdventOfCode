from get_data import get_data

import re

data = get_data(2024, 3)

pat = r"mul\((\d+),(\d+)\)"
print(sum(int(m1) * int(m2) for m1, m2 in re.findall(pat, data)))

enabled = True
part2 = 0
for m1, m2, do, dont in re.findall(pat + r"|(do\(\))|(don't\(\))", data):
    if do or dont:
        enabled = bool(do)
    else:
        part2 += int(m1) * int(m2) * enabled
print(part2)
