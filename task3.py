# task3.py
from edges import vienna_ubahn_edges
import networkx as nx
import heapq


# Створити граф
def build_graph():
    G = nx.Graph()
    for line, edges in vienna_ubahn_edges.items():
        for start, end, weight in edges:
            G.add_edge(start, end, weight=weight, line=line)
    return G


# Знайти найкоротші шляхи у графі з використанням бінарної купи (heapq)
def dijkstra_heap(graph, start):
    result = {v: [float("inf"), []] for v in graph}
    if start not in result:
        return {}

    result[start] = [0, [start]]
    heap = [(0, start)]

    while heap:
        dist, current = heapq.heappop(heap)

        if dist > result[current][0]:
            continue

        for neighbor, attrs in graph[current].items():
            new_dist = dist + attrs["weight"]
            if new_dist < result[neighbor][0]:
                result[neighbor][0] = new_dist
                result[neighbor][1] = result[current][1] + [neighbor]
                heapq.heappush(heap, (new_dist, neighbor))

    return result


if __name__ == "__main__":
    G = build_graph()
    start_station = "Neue Donau"

    shortest_paths = dijkstra_heap(G, start_station)

    for station, (dist, path) in shortest_paths.items():
        print(f"\n{station.upper()}:")
        print(f"Shortest distance: {dist:.2f} km")
        print("Path:", " => ".join(path))
