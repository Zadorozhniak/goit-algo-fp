import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Функція для побудови дерева з прикладу завдання 4
def build_sample_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root

# Функція для створення графа з бінарного дерева
def tree_to_graph(root):
    G = nx.Graph()
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node.left:
            G.add_edge(node.value, node.left.value)
            queue.append(node.left)
        if node.right:
            G.add_edge(node.value, node.right.value)
            queue.append(node.right)
    
    return G

# Функція для генерації кольорів від темних до світлих
def generate_colors(n):
    cmap = LinearSegmentedColormap.from_list("custom", ["#1296F0", "#FFFFFF"])
    colors = [cmap(i) for i in np.linspace(0, 1, n)]
    return [f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}" for r, g, b, _ in colors]

# Обхід у глибину (DFS) з використанням стеку
def dfs_traversal(root):
    if not root:
        return []
    
    visited = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        visited.append(node.value)
        
        # Додаємо спочатку правого, потім лівого нащадка для правильного порядку
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return visited

# Обхід у ширину (BFS) з використанням черги
def bfs_traversal(root):
    if not root:
        return []
    
    visited = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        visited.append(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return visited

# Функція для візуалізації обходу
def visualize_traversal(tree_root, traversal_type='dfs'):
    if traversal_type == 'dfs':
        traversal_order = dfs_traversal(tree_root)
        title = "DFS (Depth-First Search) Traversal"
    else:
        traversal_order = bfs_traversal(tree_root)
        title = "BFS (Breadth-First Search) Traversal"
    
    G = tree_to_graph(tree_root)
    pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
    
    # Генеруємо кольори для вузлів
    num_nodes = len(traversal_order)
    colors = generate_colors(num_nodes)
    
    # Створюємо фігуру
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.title(title)
    
    # Ініціалізуємо граф
    nx.draw(G, pos, with_labels=True, node_color='lightgray', ax=ax)
    
    # Функція для оновлення графіку на кожному кроці
    def update(frame):
        ax.clear()
        ax.set_title(f"{title}\nStep {frame+1}: Visiting node {traversal_order[frame]}")
        
        # Визначаємо кольори для вузлів
        node_colors = []
        for node in G.nodes():
            if node in traversal_order[:frame+1]:
                idx = traversal_order.index(node)
                node_colors.append(colors[idx])
            else:
                node_colors.append('lightgray')
        
        nx.draw(G, pos, with_labels=True, node_color=node_colors, ax=ax)
    
    # Створюємо анімацію
    ani = animation.FuncAnimation(fig, update, frames=num_nodes, interval=1000, repeat=False)
    plt.close()
    return ani

# Основна частина програми
if __name__ == "__main__":
    # Побудова дерева
    tree_root = build_sample_tree()
    
    # Візуалізація DFS
    print("DFS traversal order:", dfs_traversal(tree_root))
    dfs_ani = visualize_traversal(tree_root, 'dfs')
    dfs_ani.save('dfs_traversal.gif', writer='pillow', fps=1)
    
    # Візуалізація BFS
    print("BFS traversal order:", bfs_traversal(tree_root))
    bfs_ani = visualize_traversal(tree_root, 'bfs')
    bfs_ani.save('bfs_traversal.gif', writer='pillow', fps=1)
    
    print("Анімації збережено у файли dfs_traversal.gif та bfs_traversal.gif")