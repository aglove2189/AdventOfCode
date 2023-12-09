from get_data import get_data

data = get_data(2023, 9).splitlines()
data = [[*map(int, d.split())] for d in data]


def solve(iterable):
    diffs = [b - a for a, b in zip(iterable, iterable[1:])]
    return iterable[-1] + solve(diffs) if iterable else 0


print(sum(solve(d) for d in data))
print(sum(solve(d[::-1]) for d in data))
