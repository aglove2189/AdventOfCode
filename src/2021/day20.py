# -*- coding: utf-8 -*-
import numpy as np
from get_data import get_data
from scipy.ndimage import convolve

algo, _, *image = get_data(2021, 20).splitlines()
algo = np.array([int(p == "#") for p in algo])
image = np.pad([[int(p == "#") for p in row] for row in image], (51, 51))

for i in range(1, 51):
    image = algo[convolve(image, 2 ** np.arange(9).reshape(3, 3))]
    if i in (2, 50):
        print(image.sum())
