from functools import cache
from get_data import get_data

data = get_data(2025, 11).splitlines()

dag = {}
for d in data:
    node, targets = d.split(": ")
    dag[node] = targets.split()


@cache
def count_paths(node):
    if node == "out":
        return 1
    return sum(count_paths(n) for n in dag[node])


@cache
def count_paths2(node, seen_dac=False, seen_fft=False):
    if node == "dac":
        seen_dac = True
    if node == "fft":
        seen_fft = True
    if node == "out":
        return 1 if seen_dac and seen_fft else 0
    return sum(count_paths2(n, seen_dac, seen_fft) for n in dag[node])


print(count_paths("you"))
print(count_paths2("svr"))
