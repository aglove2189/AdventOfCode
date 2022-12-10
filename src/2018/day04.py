import collections

import dateutil
from get_data import get_data

data = get_data(2018, 4)

ttimes = collections.defaultdict(lambda: [0 for i in range(60)])

for line in sorted(data.splitlines()):
    time, action = line.split("] ")

    time = int(time.split(":")[1])

    if action.startswith("Guard"):
        guard = int(action.split()[1][1:])
    elif action == "falls asleep":
        start = time
    elif action == "wakes up":
        for i in range(start, time):
            ttimes[guard][i] += 1

m = sorted(ttimes.keys(), key=lambda x: sum(ttimes[x]), reverse=True)[0]
t = ttimes[m]
print(t.index(max(ttimes[m])) * m)

m = sorted(ttimes.keys(), key=lambda x: max(ttimes[x]), reverse=True)[0]
t = ttimes[m]
print(t.index(max(ttimes[m])) * m)
