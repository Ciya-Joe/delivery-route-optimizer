import networkx as nx
from utils import haversine

def mst_tsp(points):
    G = nx.Graph()

    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=haversine(points[i], points[j]))

    T = nx.minimum_spanning_tree(G)

    visited = []

    def dfs(node):
        visited.append(node)
        for n in T.neighbors(node):
            if n not in visited:
                dfs(n)

    dfs(0)
    return visited