import networkx as nx
from get_data import get_data

data = get_data(2025, 4).split()

rolls = {(r, c) for r, line in enumerate(data) for c, char in enumerate(line) if char == '@'}

G = nx.Graph()
G.add_nodes_from(rolls)

for r, c in rolls:
    for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:
        neighbor = (r + dr, c + dc)
        if neighbor in rolls:
            G.add_edge((r, c), neighbor)

part1 = sum(1 for _, degree in G.degree() if degree < 4)
print(part1)

part2 = G.number_of_nodes() - nx.k_core(G, k=4).number_of_nodes()
print(part2)