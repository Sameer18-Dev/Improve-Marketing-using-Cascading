# -*- coding: utf-8 -*-
"""
Created on Wed May 22 04:27:07 2019

@author: Sameer Misbah
"""



import networkx as nx
import matplotlib.pyplot as plt


g = nx.read_edgelist("DataSet.txt",create_using=nx.Graph(), nodetype = int)

print (nx.info(g))

nx.draw(g)

plt.show()







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

#G = nx.read_edgelist("Aslam.txt",create_using=nx.Graph(), nodetype = int)


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











G = nx.Graph()

G.add_edge('a', 'b', weight=3.3)
G.add_edge('b', 'c', weight=5.0)
G.add_edge('a', 'e', weight=4.6)
G.add_edge('a', 'd', weight=1.6)
G.add_edge('c', 'd', weight=2.4)
G.add_edge('c', 'e', weight=0.3)
G.add_edge('c', 'f', weight=3.0)
G.add_edge('f', 'd', weight=4.1)
G.add_edge('f', 'a', weight=2.9)
G.add_edge('e', 'd', weight=3.4)










Range01 = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 1.9]

Range02 = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] >= 2.0]

Range03 = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] >= 3.0]

Range04 = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] >= 4.0]


  # positions for all nodes
  
#pos = nx.circular_layout(G)

#pos=nx.random_layout(G)

#pos=nx.spectral_layout(G)

#pos=nx.spring_layout(G)

pos=nx.fruchterman_reingold_layout(G)



# nodes


nx.draw_networkx_edges(G, pos, edgelist=Range01,
                       width=6, edge_color='orange')

nx.draw_networkx_edges(G, pos, edgelist=Range02,
                       width=6, edge_color='yellow')

# edges
nx.draw_networkx_edges(G, pos, edgelist=Range03,
                       width=6, edge_color='y')

nx.draw_networkx_edges(G, pos, edgelist=Range04,
                       width=6, edge_color='g')


# labels

nx.draw_networkx_nodes(G, pos, node_size=1000)

labels = nx.get_edge_attributes(G,'weight')

nx.draw_networkx_edge_labels(G,pos,edge_labels=labels, font_size=10)

nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

plt.show()
