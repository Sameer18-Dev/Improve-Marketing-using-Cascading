# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt


def find(H , iteration):
    set = []
    for each in H.nodes():
        if H.degree(each) <= iteration:
            set.append(each)
    return set


def Check(H , iteration):
    Flag = 0
    for each in H.nodes():
        if H.degree(each) <= iteration:
            Flag = 1
            break
    return Flag
    





G = nx.Graph()

G.add_edges_from([(3,11),(4,5),(5,6),(5,7),(5,8),(5,9),(5,10),(10,11),(10,13),(11,13),(12,14),(12,15),(13,14),(13,15),(13,16),(13,17),(14,15),(14,16),(15,16)])


H = G.copy()
iteration = 1
Temp = []
SaveNodes = []



while(1):
    flag = Check(H , iteration)
    if flag == 0:
        iteration = iteration + 1
        SaveNodes.append(Temp)
        Temp=[]
    if flag == 1:
        nodeset = find(H , iteration)
        for each in nodeset:
            H.remove_node(each)
            Temp.append(each)
    if H.number_of_nodes() == 0:
        SaveNodes.append(Temp)
        break

print (SaveNodes)
print("Higher Degree : ", iteration)

nx.draw_networkx(G)

plt.show()