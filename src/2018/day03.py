# -*- coding: utf-8 -*-
import re

import numpy as np
from get_data import get_data

data = get_data(2018, 3)

rect = np.zeros((1000, 1000))
for r in data.split("\n"):
    pos = re.search(r"@ ([0-9,]+)", r).group(0).replace("@ ", "")
    pos = eval(pos)[::-1]
    size = re.search(r": ([0-9x]+)", r).group(0).replace(": ", "").replace("x", ",")
    size = eval(size)[::-1]

    rect[pos[0] : pos[0] + size[0], pos[1] : pos[1] + size[1]] += 1

print(rect[rect > 1].shape)

for r in data.split("\n"):
    id_ = re.search(r"#([0-9]+)", r).group(0).replace("#", "")
    pos = re.search(r"@ ([0-9,]+)", r).group(0).replace("@ ", "")
    pos = eval(pos)[::-1]
    size = re.search(r": ([0-9x]+)", r).group(0).replace(": ", "").replace("x", ",")
    size = eval(size)[::-1]

    if (rect[pos[0] : pos[0] + size[0], pos[1] : pos[1] + size[1]] == 1).all():
        print(id_)
