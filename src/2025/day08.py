from get_data import get_data
import networkx as nx
from itertools import combinations
import math

data = get_data(2025, 8).split()
points = [tuple(map(int, d.split(","))) for d in data]

all_edges = []
for u, v in combinations(range(len(points)), 2):
    dist = math.dist(points[u], points[v])
    all_edges.append((u, v, dist))

all_edges.sort(key=lambda x: x[2])

G = nx.Graph()
G.add_weighted_edges_from(all_edges[:1000])

circuits = [len(c) for c in sorted(nx.connected_components(G), key=len)]
print(math.prod(circuits[-3:]))

G.add_weighted_edges_from(all_edges)

mst = nx.minimum_spanning_tree(G)
last_edge = max(mst.edges(data=True), key=lambda x: x[2]["weight"])
u, v, _ = last_edge
print(points[u][0] * points[v][0])
