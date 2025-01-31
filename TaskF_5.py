import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex, to_rgb
import numpy as np

class Node:
    def __init__(self, key, color="#87CEEB"):
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())
        self.visited = False

def add_tree_edges(graph, tree, pos, x=0, y=0, layer=1):
    if tree is not None:
        graph.add_node(tree.id, color=tree.color, label=tree.val)
        pos[tree.id] = (x, y)

        if tree.left:
            graph.add_edge(tree.id, tree.left.id)
            add_tree_edges(graph, tree.left, pos, x - 1 / 2 ** layer, y - 1, layer + 1)

        if tree.right:
            graph.add_edge(tree.id, tree.right.id)
            add_tree_edges(graph, tree.right, pos, x + 1 / 2 ** layer, y - 1, layer + 1)

def draw_tree(tree, highlight_path=None):
    graph = nx.DiGraph()
    pos = {}
    add_tree_edges(graph, tree, pos)

    if highlight_path:
        for node in highlight_path:
            node.color = highlight_path[node]

    colors = [node[1]['color'] for node in graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def bfs_traversal(tree):
    queue = [tree]
    step = 0
    highlight_path = {}

    while queue:
        current = queue.pop(0)
        highlight_path[current] = generate_color(step)
        draw_tree(tree, highlight_path)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

        step += 2

def dfs_traversal(tree):
    stack = [tree]
    step = 0
    highlight_path = {}

    while stack:
        current = stack.pop()
        highlight_path[current] = generate_color(step)
        draw_tree(tree, highlight_path)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

        step += 2

def generate_color(step):
    max_steps = 16
    factor = step / max_steps
    base_color = np.array(to_rgb("#1296F0"))
    white = np.array(to_rgb("#FFFFFF"))
    return to_hex(base_color * (1 - factor) + white * factor)

class BinaryTreeNode(Node):
    def __init__(self, key, color="#87CEEB"):
        super().__init__(key, color)
        self.left = None
        self.right = None

root = BinaryTreeNode(0)
root.left = BinaryTreeNode(4)
root.right = BinaryTreeNode(1)
root.left.left = BinaryTreeNode(5)
root.left.right = BinaryTreeNode(10)
root.right.left = BinaryTreeNode(3)

print("BFS Traversal")
bfs_traversal(root)

print("DFS Traversal")
dfs_traversal(root)
