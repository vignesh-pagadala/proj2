# Project 2
# Get graph from CSV and run simulation.
# Includes code for cure

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

# Initial inoculated node.
initInocNode = int(sys.argv[5])

# Probability with which to infect the node.
p = float(sys.argv[2])
p1 = float(sys.argv[4])
           
# Initially, all nodes are uninfected, so set them all to uinf.
# ALSO SET ATTRIBUTE 'cured' TO no.
           

nx.set_node_attributes(G2, name = 'status', values = 'uinf')
nx.set_node_attributes(G2, name = 'cured', values = 'no')

# Now, choose init worm node, and set status to inf.
nx.set_node_attributes(G2, name = 'status', values = {initNode : 'inf'})
# Choose init cure node and set status to yes.
nx.set_node_attributes(G2, name = 'cured', values = {initInocNode : 'yes'})
           
# ------------------------------
# Simulation.
# ------------------------------

roundcount = 0
infectedperround = []
inocperround = []

while(1):
    inocNodeList = []
    infectedNodeList = []
    # Get list of infected nodes.
    for n in G2.nodes():
        if (G2.node[n]['status'] == 'inf'):
            infectedNodeList.append(n)
    infectionCount = len(infectedNodeList)

    # Get list of inoculated nodes.
    for n in G2.nodes():
        if G2.node[n]['cured'] == 'yes':
            inocNodeList.append(n)
    inoccount = len(inocNodeList)
    
    # Iterate through these infected nodes and check for neighbour which is uinf.
    # In which case, evaluate probability and infect.
    # INFECTION   
    for n in infectedNodeList:
        neighboursList = G2.neighbors(n)
        for node in neighboursList:
            # If node is uninfected, and uninoculated then infect with prob.
            if((G2.node[node]['status'] == 'uinf') and (G2.node[node]['cured'] == 'no')):
                 percent = p * 100
                 if(random.randint(0,100) < percent):
                     # Infect node.
                     nx.set_node_attributes(G2, name = 'status', values = {node : 'inf'})
                    
    # INOCULATION
    
    for n in inocNodeList:
        neighboursList = G2.neighbors(n)
        for node in neighboursList:
                       # If node is uninoculated, then inoculate with prob p1, and cure.
            if(G2.node[node]['cured'] == 'no'):
                 percent = p1 * 100
                 if(random.randint(0,100) < percent):
                     # Inoculate node.
                     nx.set_node_attributes(G2, name = 'cured', values = {node : 'yes'})
                     # Cure node.
                     nx.set_node_attributes(G2, name = 'status', values = {node : 'uinf'})
                     inoccount += 1  
    print(inocNodeList)            
    roundcount += 1
    infectedperround.append(infectionCount)
    inocperround.append(inoccount)
    if(len(inocNodeList) == len(G2)):
        break
   
print("Number of infected nodes: ", len(infectedNodeList))
print("Number of inoc node: ", len(inocNodeList))
print("Number of rounds: ", roundcount)
print("Inoculation: ", inocperround)
print("Infected: ", infectedperround)
# To visualize.
#nx.draw(G2, nx.spring_layout(G2))
#node_labels = nx.get_node_attributes(G2,'status')
#nx.draw_networkx_labels(G2, nx.spring_layout(G2), labels = node_labels)

plt.plot(infectedperround)
plt.title('Rate of Worm Spread for an Watts-Strogatz Network with Cure Applied')
plt.xlabel('Round')
plt.ylabel('Number of Infected Nodes')
plt.show()




    
