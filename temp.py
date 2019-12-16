# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import networkx as nx
import matplotlib.pyplot as plt
import csv


g = nx.read_edgelist("DataSet.txt",create_using=nx.Graph(), nodetype = int)

print (nx.info(g))

nx.draw(g)

plt.show()
