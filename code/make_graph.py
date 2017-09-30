import networkx as nx
import pandas as pd
import numpy as np
from import_owtrad import import_owtrad
import matplotlib.pyplot as plt


# new_csv = pd.read_csv('./OWTRAD-Files/OWTRAD-South German trade routes before 1500 CE-routes.csv'.strip(), header=0)
# print(new_csv.iloc[10])

nodes, edges = import_owtrad()

print(len(nodes))

edges_list = zip(edges['NODE1'], edges['NODE2'])
# print(next(edges_list))

G = nx.Graph()
G.add_edges_from(edges_list)

print(len(G.nodes()))

def draw_graph(G):
    nx.draw_circular(G,
                     node_size=100,
                     with_labels=True)
    plt.show()

draw_graph(G)

# print(nodes.info())
# print()
# print(edges.info())
