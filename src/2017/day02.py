# -*- coding: utf-8 -*-
from get_data import get_data

import itertools
import io
import pandas as pd


data = get_data(2017, 2)

array = pd.read_table(io.StringIO(data), header=None).values

print(sum(abs(max(a) - min(a)) for a in array))

print(sum([a // b for arr in array 
            for a, b in itertools.product(arr, arr) 
            if a > b and a % b == 0]))
