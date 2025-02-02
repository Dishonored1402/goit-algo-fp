import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_heap_edges(graph, heap, pos, index=0, x=0, y=0, dx=1.5):
    """Рекурсивно додає вузли та ребра для візуалізації купи."""
    if index >= len(heap):
        return
    
    node = heap[index]
    graph.add_node(node.id, color=node.color, label=node.val)
    pos[node.id] = (x, y)
    
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    
    if left_index < len(heap):
        left_node = heap[left_index]
        graph.add_edge(node.id, left_node.id)
        add_heap_edges(graph, heap, pos, left_index, x - dx, y - 1, dx / 2)
    
    if right_index < len(heap):
        right_node = heap[right_index]
        graph.add_edge(node.id, right_node.id)
        add_heap_edges(graph, heap, pos, right_index, x + dx, y - 1, dx / 2)

def draw_heap(heap):
    tree = nx.DiGraph()
    pos = {}
    add_heap_edges(tree, heap, pos)

    colors = [tree.nodes[node]['color'] for node in tree.nodes]
    labels = {node: tree.nodes[node]['label'] for node in tree.nodes}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

heap = [
    Node(10),
    Node(9),
    Node(8),
    Node(7),
    Node(6),
    Node(5),
    Node(4)
]

draw_heap(heap)
