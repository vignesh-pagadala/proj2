
# Project 2
# Author: Vignesh M. Pagadala
# Date: 03/18/18

import numpy as np
import csv
import sys
import networkx as nx
import matplotlib.pyplot as plt
'''
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_edge(1,2)
G.add_edge(3,4)
nx.draw(G)
plt.show()
'''
'''
G = nx.erdos_renyi_graph(5, 0.4)
nx.draw(G)
nx.draw_networkx_labels(G, pos = nx.spring_layout(G))
print("\nNumber of nodes: ", G.number_of_edges())
edgeList = G.edges()
print("\nEdges: ",edgeList)
plt.show()
'''

# Creating graph and writing to CSV file. 
G = nx.erdos_renyi_graph(300, 0.3)
edgeList = G.edges()
edgeList = list(edgeList)
print(G.number_of_edges())
# Write edgeList to .csv file.
with open('graph1.csv','w') as out:
    csv_out=csv.writer(out)
    for row in edgeList:
        csv_out.writerow(row)



