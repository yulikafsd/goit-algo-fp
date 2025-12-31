from collections import deque
from matplotlib import colors
from task3 import build_graph
from task4 import graph_to_heap_by_line, heap_to_tree, draw_tree


# DFS обхід без рекурсії
def dfs(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # Додаємо правого спочатку, щоб лівий відвідувався першим
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return visited


# BFS обхід без рекурсії
def bfs(root):
    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return visited


# Генерація кольорів для вузлів
def color_nodes(order, start_color="#003366", end_color="#99CCFF"):
    sr, sg, sb = colors.to_rgb(start_color)
    er, eg, eb = colors.to_rgb(end_color)

    total = len(order)
    for i, node in enumerate(order):
        r = sr + (er - sr) * i / max(total - 1, 1)
        g = sg + (eg - sg) * i / max(total - 1, 1)
        b = sb + (eb - sb) * i / max(total - 1, 1)
        node.color = (r, g, b)


if __name__ == "__main__":
    G = build_graph()
    line = "U3"
    heap = graph_to_heap_by_line(G, line)
    root = heap_to_tree(heap)

    if root is None:
        print(f"Дерево для лінії {line} порожнє")
    else:
        # ----- DFS -----
        dfs_order = dfs(root)
        color_nodes(dfs_order)
        draw_tree(root)

        # ----- BFS -----
        bfs_order = bfs(root)
        color_nodes(bfs_order)
        draw_tree(root)
