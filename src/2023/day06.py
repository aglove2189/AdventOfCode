import math

from get_data import get_data


def solve(time, distance):
    return sum([i * (time - i) > distance for i in range(1, time + 1)])


data = get_data(2023, 6)
times, distances = data.splitlines()
times = list(map(int, times.split()[1:]))
distances = list(map(int, distances.split()[1:]))

print(math.prod([solve(time, distance) for time, distance in zip(times, distances)]))
print(solve(int("".join(map(str, times))), int("".join(map(str, distances)))))
