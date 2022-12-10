import operator
from functools import reduce
from itertools import combinations

from get_data import get_data

data = get_data(2020, 1)
data = list(map(int, data.split()))


def func(data, r=2):
    for c in combinations(data, r):
        if sum(c) == 2020:
            return reduce(operator.mul, c)


print(func(data))
print(func(data, r=3))
