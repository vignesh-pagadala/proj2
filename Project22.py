# Project 2
# Get graph from CSV and run simulation.

import csv
import networkx as nx
import matplotlib.pyplot as plt
'''
with open('graph1.csv', 'r') as f:
    reader = csv.reader(f)
    edgeList = list(reader)

edgeList = [[int(float(j)) for j in i] for i in edgeList]

G = nx.Graph()

G.add_edges_from(edgeList)
'''
G2 = nx.Graph()
G2.add_edge(1,2)
G2.add_edge(2,3)
G2.add_edge(2,4)

'''
nx.set_node_attributes(G2, name = 'Infected', values = 'n')
nx.set_node_attributes(G2, name = 'Infected', values = {1:'y'})

nodesAt5 = []

for n in G2.nodes():
    if G2.node[n]['Infected'] == 'y':
        nodesAt5.append(n)
print(nodesAt5)
'''

# The initial infected node.
initNode = 1

# Initially, all nodes are uninfected, so set them all to uinf.
nx.set_node_attributes(G2, name = 'status', values = 'uinf')

# Now, choose init node, and set status to inf.
nx.set_node_attributes(G2, name = 'status', values = {initNode : 'inf'})

# Get list of nodes which are adjacent to an infected node, and uninfected.
# Get list of all infected nodes in graph.
infectedNodeList = []

for n in G2.nodes():
    if G2.node[n]['status'] == 'inf':
        infectedNodeList.append(n)
print(infectedNodeList)

# To visualize.
nx.draw(G2, nx.spring_layout(G2))
node_labels = nx.get_node_attributes(G2,'status')
nx.draw_networkx_labels(G2, nx.spring_layout(G2), labels = node_labels)

plt.show()




    
