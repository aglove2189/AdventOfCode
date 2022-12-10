# -*- coding: utf-8 -*-
from itertools import product

import networkx as nx
import numpy as np
from get_data import get_data

data = get_data(2021, 15).splitlines()
data = [[int(y) for y in x] for x in data]


def find_path(data):
    n = len(data)
    G = nx.grid_2d_graph(n, n, create_using=nx.DiGraph())
    for i, j in G.edges:
        G[i][j]['weight'] = data[j[1]][j[0]]
    return nx.shortest_path_length(G, source=(0, 0), target=(n - 1, n - 1), weight='weight')


print(find_path(data))

n = len(data)
data2 = np.zeros((n * 5, n * 5), dtype=np.uint8)
for row, col in product(range(n * 5), range(n * 5)):
    data2[col][row] = data[col % n][row % n] + (row // n) + (col // n)
data2[data2 > 9] -= 9
print(find_path(data2))
