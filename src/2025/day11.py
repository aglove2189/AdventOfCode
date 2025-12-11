from functools import cache
from get_data import get_data


@cache
def solve(node, t="out"):
    return 1 if node == t else sum(solve(n, t) for n in dag.get(node, []))


data = get_data(2025, 11).splitlines()
dag = {k: v.split() for d in data for k, v in [d.split(": ")]}

print(solve("you"))
route1 = solve("svr", "dac") * solve("dac", "fft") * solve("fft", "out")
route2 = solve("svr", "fft") * solve("fft", "dac") * solve("dac", "out")
print(route1 + route2)
