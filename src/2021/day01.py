# -*- coding: utf-8 -*-
import pandas as pd
from get_data import get_data

data = get_data(2021, 1)
s = pd.Series(data.split()).astype(int)

part1 = (s > s.shift()).sum()
print(part1)

rolling = s.rolling(3).sum()
part2 = (rolling > rolling.shift()).sum()
print(part2)
