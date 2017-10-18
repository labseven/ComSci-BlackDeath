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

city_i = 5
thinkplot.plot(history[city_i,4,:])
plt.title("Infected at each timestep, degree" + str(len(G[node_list[city_i]])))
thinkplot.show()

# thinkplot.plot(history[1,:3,:100].T)
# thinkplot.show()

thinkplot.Plot(np.sum(history[:, 0, :], axis=0), label="Susceptible")
thinkplot.Plot(np.sum(history[:, 1, :], axis=0), label="Infected")
thinkplot.Plot(np.sum(history[:, 2, :], axis=0), label="Dead")
thinkplot.Plot(np.sum(history[:, 3, :], axis=0), label="R")
plt.title("Population distribution in entire simulation")
plt.xlabel("Timestep")
plt.ylabel("Population")
thinkplot.config(legend=True)
thinkplot.show()


thinkplot.Plot(history[0, 0, :], label="Susceptible")
thinkplot.Plot(history[0, 1, :], label="Infected")
thinkplot.Plot(history[0, 2, :], label="Dead")
thinkplot.Plot(history[0, 3, :], label="R")
plt.title("Population distribution in one city")
plt.xlabel("Timestep")
plt.ylabel("Population")
thinkplot.config(legend=True)
thinkplot.show()



print("num infected", history[:,4,:])

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
    infections_per_city[city] = np.sum(history[node_index(city), 4, :])


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


"""
# Analytics
# print(len(cur_infected))
# print([(city, infected_times[city]) for city in infected_times if infected_times[city]])


# Sum the number of times each city has been infected
# infections_per_city = dict()
# for city in infected_timestamps:
#     infections_per_city[city] = len(infected_timestamps[city])


# infection_cdf = Cdf(infection_count.values())
# t.Cdf(infection_cdf)
# thinkplot.show()


# Plotting degree distribution
degree_of_node = dict()
for node in G.nodes():
    degree_of_node[node] = len(G[node])


def degree_pmf_graph(G):
    degree_of_G_pmf = dict()
    for node in G.nodes():
        try:
            degree_of_G_pmf[len(G[node])] += 1
        except KeyError:
            degree_of_G_pmf[len(G[node])] = 1
    return degree_of_G_pmf

degree_of_G_pmf = degree_pmf_graph(G)
degree_of_trade_pmf = degree_pmf_graph(network_trade)
degree_of_pilgrimadge_pmf = degree_pmf_graph(network_pilgrimadge)

print("mean degree:", np.mean(list(degree_of_node.values())))

# print(degree_of_G_pmf, degree_of_G_pmf.values())
print(degree_of_trade_pmf)
print(list(degree_of_trade_pmf.keys()))
print(list(degree_of_trade_pmf.values()))


plt.title('Our Degree Distribution')
thinkplot.Plot(list(degree_of_G_pmf.keys()), list(degree_of_G_pmf.values()), label="Combined Network")
thinkplot.Plot(list(degree_of_trade_pmf.keys()), list(degree_of_trade_pmf.values()), label="Trade Network")
thinkplot.Plot(list(degree_of_pilgrimadge_pmf.keys()), list(degree_of_pilgrimadge_pmf.values()), label="Pilgrimadge Network")
# thinkplot.show()


plt.title('Degree Distribution Cdf')
degree_cdf = Cdf(degree_of_node.values())
thinkplot.Cdf(degree_cdf)
# thinkplot.show()

# for degree in range(degree_of_node.values().max(), 0, -1):

# print(nodes.info())
# print()
# print(edges.info())
"""
