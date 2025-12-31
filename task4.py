import heapq
import uuid
import networkx as nx
import matplotlib.pyplot as plt
from task3 import build_graph


# Ініціалізуємо вузол
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


# Перетворюємо граф на купу, використовуючи ребра однієї лінії метро
def graph_to_heap_by_line(graph, line_name):
    heap = []
    used = set()

    for u, v, data in graph.edges(data=True):
        if data.get("line") == line_name:
            if (u, v) not in used and (v, u) not in used:
                u_short = "".join(word[0].upper() for word in u.split())
                v_short = "".join(word[0].upper() for word in v.split())
                label = f"{u_short} → {v_short}"
                heapq.heappush(heap, (data["weight"], label))
                used.add((u, v))

    return heap


# Перетворюємо купу на дерево
def heap_to_tree(heap):
    if not heap:
        return None

    nodes = [Node(f"{w:.2f} км\n{label}") for w, label in heap]

    for i in range(len(nodes)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(nodes):
            nodes[i].left = nodes[left]
        if right < len(nodes):
            nodes[i].right = nodes[right]

    return nodes[0]


# Візуалізація дерева
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, l, y - 1, layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, r, y - 1, layer + 1)


def draw_tree(root):
    if root is None:
        print("Tree is empty")
        return

    graph = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(graph, root, pos)

    colors = [data["color"] for _, data in graph.nodes(data=True)]
    labels = {n: data["label"] for n, data in graph.nodes(data=True)}

    plt.figure(figsize=(12, 6))
    nx.draw(graph, pos, labels=labels, node_color=colors, node_size=2500, arrows=False)
    plt.show()


if __name__ == "__main__":
    G = build_graph()
    line = "U1"
    heap = graph_to_heap_by_line(G, line)
    root = heap_to_tree(heap)
    print(f"Візуалізація бінарної купи для лінії {line}")
    draw_tree(root)
