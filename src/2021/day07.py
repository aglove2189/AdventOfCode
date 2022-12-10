# -*- coding: utf-8 -*-
import numpy as np
from get_data import get_data

data = list(map(int, get_data(2021, 7).split(",")))

print(int(sum(abs(data - np.median(data)))))

def cost(x): return x * (x + 1) // 2
print(min([sum(cost(abs(x - d)) for x in data) for d in data]))
