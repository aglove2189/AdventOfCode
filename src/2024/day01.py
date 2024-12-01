from get_data import get_data

data = list(map(int, get_data(2024, 1).split()))
first = data[0::2]
second = data[1::2]
print(sum([abs(x - y) for x, y in zip(sorted(first), sorted(second))]))
print(sum([i * second.count(i) for i in first]))
