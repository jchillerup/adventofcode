import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

for line in open('input.txt').readlines():
    src, dst = line.strip().split("-")

    G.add_node(src)
    G.add_node(dst)
    G.add_edge(src, dst)

def is_lowercase(s):
    return s == s.lower()

def traverse(node, path=[]):
    if is_lowercase(node) and node in path: return
    
    new_path = list(path)
    new_path.append(node)

    if node == "end":
        print(new_path)

    for neighbor in G[node]:
        traverse(neighbor, new_path)

traverse("start", [])