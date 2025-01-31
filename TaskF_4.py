import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_heap_edges(graph, heap, pos, x=0, y=0, layer=1):
    n = len(heap)
    for i in range(n):
        node = heap[i]
        graph.add_node(node.id, color=node.color, label=node.val)
        pos[node.id] = (x, y)
        
        left_index = 2 * i + 1
        if left_index < n:
            left_node = heap[left_index]
            graph.add_edge(node.id, left_node.id)
            pos[left_node.id] = (x - 1 / 2 ** layer, y - 1)
        
        right_index = 2 * i + 2
        if right_index < n:
            right_node = heap[right_index]
            graph.add_edge(node.id, right_node.id)
            pos[right_node.id] = (x + 1 / 2 ** layer, y - 1)
        
        x += 1 / 2 ** layer

    return graph

def draw_heap(heap):
    tree = nx.DiGraph()
    pos = {}
    tree = add_heap_edges(tree, heap, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

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
