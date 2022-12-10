import pandas as pd
from get_data import get_data

data = sorted(list(map(int, get_data(2020, 10).splitlines())))
data.insert(0, 0)
data.append(max(data) + 3)

s = pd.Series(data).diff()
print(len(s[s == 3]) * len(s[s == 1]))

chains = [1] + [0] * (len(data) - 1)
for i in range(1, len(chains)):
    for j in range(0, i):
        if data[i] - data[j] <= 3:
            chains[i] += chains[j]
print(max(chains))
