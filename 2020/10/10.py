numbers = [int(x) for x in open('input.txt', 'r').read().strip().split("\n")]
numbers.sort()
diffs = [numbers[x]-numbers[x-1] for x in range(1,len(numbers))]
print((1+diffs.count(1)) * (1+diffs.count(3)))

numbers.append(0)
numbers.append(max(numbers)+3)
numbers.sort()

import matplotlib.pyplot as plt
import networkx as nx
G = nx.DiGraph()
G.add_nodes_from(numbers)

for number in numbers:
    if number+1 in numbers:
        G.add_edge(number, number+1)
    if number+2 in numbers:
        G.add_edge(number, number+2)
    if number+3 in numbers:
        G.add_edge(number, number+3)

tail = 0
mult = 1
for node in G:
    if G.in_degree(node) == 1 and (G.out_degree(list(G.predecessors(node))[0]) == 1):
        mult *= len(list(nx.all_simple_paths(G, tail, node)))
        tail = node
print(mult)

#nx.draw_circular(G, with_labels=True)
#plt.show()