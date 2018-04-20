# Project 2
# Get graph from CSV and run simulation.
import random
import csv
import networkx as nx
import matplotlib.pyplot as plt
import time
import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    reader = csv.reader(f)
    edgeList = list(reader)

edgeList = [[int(float(j)) for j in i] for i in edgeList]

G2 = nx.Graph()
G2.add_edges_from(edgeList)

# The initial infected node.
initNode = int(sys.argv[3])

# Probability with which to infect the node.
p = float(sys.argv[2])

# Initially, all nodes are uninfected, so set them all to uinf.
nx.set_node_attributes(G2, name = 'status', values = 'uinf')

# Now, choose init node, and set status to inf.
nx.set_node_attributes(G2, name = 'status', values = {initNode : 'inf'})

# ------------------------------
# Simulation.
# ------------------------------

# Initialize value.
nextNodeToInfect = 1
# Get list of nodes which are adjacent to an infected node, and uninfected.
# Get list of all infected nodes in graph.
roundcount = 0
infectedperround = []
while(1):
    infectionCount = 0
    infectedNodeList = []
    # Get list of infected nodes.
    for n in G2.nodes():
        if G2.node[n]['status'] == 'inf':
            infectedNodeList.append(n)
        
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
    infectionCount += 1
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
                infectionCount += 1
    # Now, one round is complete.
    roundcount += 1
    infectedperround.append(infectionCount)
    #print("Number of infected nodes: ", len(infectedNodeList))

print("Number of rounds: ", roundcount)
print(infectedperround)
# To visualize.
#nx.draw(G2, nx.spring_layout(G2))
#node_labels = nx.get_node_attributes(G2,'status')
#nx.draw_networkx_labels(G2, nx.spring_layout(G2), labels = node_labels)

plt.plot(infectedperround)
plt.show()




    
