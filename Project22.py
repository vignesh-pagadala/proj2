# Project 2
# Get graph from CSV and run simulation.
import random
import csv
import networkx as nx
import matplotlib.pyplot as plt
import time

with open('graph1.csv', 'r') as f:
    reader = csv.reader(f)
    edgeList = list(reader)

edgeList = [[int(float(j)) for j in i] for i in edgeList]

G2 = nx.Graph()
G2.add_edges_from(edgeList)

'''
G2 = nx.Graph()
G2.add_edge(1,2)
G2.add_edge(2,3)
G2.add_edge(2,4)
'''

# The initial infected node.
initNode = 1

# Probability with which to infect the node.
p = 0.5

# Initially, all nodes are uninfected, so set them all to uinf.
nx.set_node_attributes(G2, name = 'status', values = 'uinf')

# Now, choose init node, and set status to inf.
nx.set_node_attributes(G2, name = 'status', values = {initNode : 'inf'})

# ------------------------------
# Selecting next node to infect.
# ------------------------------

# Initialize value.
nextNodeToInfect = 1
# Get list of nodes which are adjacent to an infected node, and uninfected.
# Get list of all infected nodes in graph.
roundcount = 0
while(1):
    print("Round complete")
    infectedNodeList = []
    # Get list of infected nodes.
    for n in G2.nodes():
        if G2.node[n]['status'] == 'inf':
            infectedNodeList.append(n)
   # print(infectedNodeList)
    
    # Iterate through these infected nodes and check for neighbour which is uinf.
    nodeFoundFlag = 0
    for n in infectedNodeList:
        if(nodeFoundFlag == 1):
            break
        neighboursList = G2.neighbors(n)
        for node in neighboursList:
            if(G2.node[node]['status'] == 'uinf'):
                nextNodeToInfect = node
                nodeFoundFlag = 1
                break
    if(len(infectedNodeList) == len(G2)):
        break

    # Infect this selected  node.
    nx.set_node_attributes(G2, name = 'status', values = {nextNodeToInfect : 'inf'})
    
    # Create a list of nodes adjacent to this selected node.
    adjNodes = list(G2.neighbors(nextNodeToInfect))
    # Iterate through this list.
    # If node is not infected, evaluate it with probability of p, and infect it.
    for node in adjNodes:
        if(G2.node[node]['status'] == 'uinf'):
            # Evaluate probability.
            percent = p * 100
            if(random.randint(0,100) < percent):
                # Infect node.
                nx.set_node_attributes(G2, name = 'status', values = {node : 'inf'})

    # Now, one round is complete.
    roundcount += 1
    print("Number of infected nodes: ", len(infectedNodeList))

# To visualize.
nx.draw(G2, nx.spring_layout(G2))
node_labels = nx.get_node_attributes(G2,'status')
nx.draw_networkx_labels(G2, nx.spring_layout(G2), labels = node_labels)

plt.show()




    
