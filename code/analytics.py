import networkx as nx
import numpy as np
import sys
import _pickle

from import_owtrad import import_owtrad

import matplotlib.pyplot as plt

import thinkplot
import thinkstats2
from thinkstats2 import Cdf, Pmf

# Import the OWTRAD dataset
nodes, edges = import_owtrad()


# Select the edges that we want to use
edges_to_use = edges.loc[(edges.USES == 'trd') | (edges.USES == 'plg')]
edges_list = zip(edges_to_use['NODE1'], edges_to_use['NODE2'])


nodes2, edges2 = import_owtrad()


# Select the edges that we want to use
edges_to_use2 = edges2.loc[(edges2.USES == 'trd') | (edges2.USES == 'plg')]
edges_list2 = zip(edges_to_use2['NODE1'], edges_to_use2['NODE2'])


# Make nx graph
G = nx.Graph()
G.add_edges_from(edges_list)


history = _pickle.load(open("{}.pkl".format(sys.argv[1]), "rb"))
node_list = _pickle.load(open("{}_nodelist.pkl".format(sys.argv[1]), "rb"))


# print(len(history))
# print(len(history[history[:,0,50] == 100, :, 50]))
# print(len(history[history[:,0,50] > 50, :, 50]))
# print(len(history[history[:,0,50] < 50, :, 50]))



# thinkplot.plot(history[1,:3,:100].T)
# thinkplot.show()

thinkplot.Plot(np.sum(history[:, 0, :], axis=0), label="Susceptible")
thinkplot.Plot(np.sum(history[:, 1, :], axis=0), label="Infected")
thinkplot.Plot(np.sum(history[:, 2, :], axis=0), label="Dead")
plt.title("Sum alive in all of Europe")
thinkplot.config(legend=True)
thinkplot.show()


print("num infected", history[:,3,:])

thinkplot.plot(np.sum(history[:,3,:], axis=1))
thinkplot.show()


""" Plot CDF of infections number """
infection_cdf = Cdf(np.sum(history[:,3,:], axis=1))
thinkplot.Cdf(infection_cdf)
plt.title("Sum Reinfections Cdf")
plt.xlabel("Total Reinfections")
plt.ylabel("CDF")
thinkplot.show()



# print("G Len nodes:", len(G.nodes()))
# print("G Len edges:", len(G.edges()))
# print("G transitivity:", nx.transitivity(G))
# print("G Degree Centrality:", np.mean(list(nx.degree_centrality(G).values())))
# # print("G Closeness Centrality:", np.mean(list(nx.closeness_centrality(G).values())))
# print("G Clustering:", nx.average_clustering(G))



""" Plot infections vs degree and closeness """
def node_index(city):
    return node_list.index(city)

infections_per_city = dict()
for city in node_list:
    infections_per_city[city] = np.sum(history[node_index(city), 3, :])


degree_vs_infections = np.zeros((len(node_list), 2))
degree_centrality = nx.degree_centrality(G)
for i, city in enumerate(node_list):
    degree_vs_infections[i] = (degree_centrality[city], infections_per_city[city])

thinkplot.Scatter(degree_vs_infections[:, 0], degree_vs_infections[:, 1])
plt.title("Degree vs Reinfections")
plt.xlabel("Degree Centrality")
plt.ylabel("Reinfections")
thinkplot.show()



closeness_vs_infections = np.zeros((len(node_list), 2))
closeness_centrality = nx.closeness_centrality(G)
for i, city in enumerate(node_list):
    closeness_vs_infections[i] = (closeness_centrality[city], infections_per_city[city])


thinkplot.Scatter(closeness_vs_infections[:, 0], closeness_vs_infections[:, 1])
plt.title("closeness_vs_infections")
thinkplot.show()
