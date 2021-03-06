
# Project 2
# Author: Vignesh M. Pagadala
# Date: 03/18/18
# Creating graph .csv files.


import numpy as np
import csv
import sys
import networkx as nx
import matplotlib.pyplot as plt

# Creating graph and writing to CSV file.

# Erdos-Renyi graph
#G = nx.erdos_renyi_graph(1500, 0.3)

# Barabasi Albert graph
#G = nx.barabasi_albert_graph(10, 3)

# Watts-Strogatz graph
G = nx.watts_strogatz_graph(500, 5, 0.6)

print(G.number_of_edges())

#nx.draw_networkx_labels(G, pos=nx.spring_layout(G))
#nx.draw(G)
#plt.show()

edgeList = G.edges()
edgeList = list(edgeList)
print(G.number_of_edges())
# Write edgeList to .csv file.
with open('Watts_Strogatz_1500.csv','w') as out:
    csv_out=csv.writer(out)
    for row in edgeList:
        csv_out.writerow(row)


