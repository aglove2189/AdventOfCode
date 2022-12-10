from collections import Counter

from get_data import get_data

data = get_data(2015, 3)

pos = [0, 0]
c = Counter()

for d in data:
    if d == "v":
        pos[1] -= 1
    elif d == "^":
        pos[1] += 1
    elif d == ">":
        pos[0] += 1
    elif d == "<":
        pos[0] -= 1

    c[tuple(pos)] += 1
print(len(c))


s_pos = [0, 0]
r_pos = [0, 0]
c = Counter()

for idx, d in enumerate(data):
    if idx % 2 == 0:
        pos = s_pos
    else:
        pos = r_pos

    if d == "v":
        pos[1] -= 1
    elif d == "^":
        pos[1] += 1
    elif d == ">":
        pos[0] += 1
    elif d == "<":
        pos[0] -= 1

    c[tuple(pos)] += 1
print(len(c))
