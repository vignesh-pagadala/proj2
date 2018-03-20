
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
G = nx.erdos_renyi_graph(500, 0.3)
edgeList = G.edges()
edgeList = list(edgeList)
print(G.number_of_edges())
# Write edgeList to .csv file.
with open('Edros_Renyi_500.csv','w') as out:
    csv_out=csv.writer(out)
    for row in edgeList:
        csv_out.writerow(row)



