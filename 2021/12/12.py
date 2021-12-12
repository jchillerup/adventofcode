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

def path_saturated(path):
    path.sort()
    for idx, p in enumerate(path):
        if idx == 0: continue

        if is_lowercase(p) and p == path[idx-1]:
            return True
    return False

def may_visit(s, path):
    if s == "start" and len(path) > 0:
        return False
    
    if is_lowercase(s) and s in path and path_saturated(path):
        return False
    
    return True

def traverse(node, path=[]):
    if not may_visit(node, path): return

    if node == "end":
        print(path+[node])
        return

    for neighbor in G[node]:
        traverse(neighbor, path+[node])

traverse("start", [])