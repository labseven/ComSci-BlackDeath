import networkx as nx
import pandas as pd
import numpy as np
from import_owtrad import import_owtrad
import matplotlib.pyplot as plt
import thinkplot
import thinkstats2
from thinkstats2 import Cdf, Pmf

# new_csv = pd.read_csv('./OWTRAD-Files/OWTRAD-South German trade routes before 1500 CE-routes.csv'.strip(), header=0)
# print(new_csv.iloc[10])

nodes, edges = import_owtrad()


trade_edges = edges[edges['USES'] == 'trd']
pilgrimadge_edges = edges[edges['USES'] == 'plg']

print("Len trade routes:", len(trade_edges))
print("Len pilgrimadeg routes:", len(pilgrimadge_edges))

# print(pilgrimadge_edges)

edges_list = zip(edges['NODE1'], edges['NODE2'])
# print(next(edges_list))

G = nx.Graph()
G.add_edges_from(edges_list)

print("Len nodes:", len(G.nodes()))
print("Len edges:", len(G.edges()))
# print(G.nodes())

def draw_graph(G):
    nx.draw_circular(G,
                     node_size=100,
                     with_labels=True)
    plt.show()

# draw_graph(G)



infected_times = dict.fromkeys(G.nodes(), frozenset())
infected_set = set(['Etil','Bukhara'])
i = 0
for city in infected_set:
    infected_times[city] = infected_times[city].union(set([i]))

print(infected_times["Etil"], infected_times['Srem'], infected_times['Trembowla'])


def toss(p):
    return np.random.ranf() < p

def step_infect(G, infected_set, p):
    new_infected = set()
    for infected_city in infected_set:
        neighbors = G[infected_city]
        for city in neighbors:
            if toss(p):
                new_infected.add(city)
    return new_infected

total_infection = 0
p = .1

while (total_infection < 6 * len(G.nodes())): # 6 * len(G.nodes()
    new_infected = step_infect(G, infected_set, p)
    for city in new_infected:
        infected_set.add(city)
    total_infection += len(new_infected)
    for city in new_infected:
        infected_times[city] = infected_times[city].union(set([i]))

    i+=1

print(len(infected_set))
# print([(city, infected_times[city]) for city in infected_times if infected_times[city]])

infection_count = dict()
for city in infected_times:
    infection_count[city] = len(infected_times[city])

# infection_cdf = Cdf(infection_count.values())
# thinkplot.Cdf(infection_cdf)
# thinkplot.show()

degree_of_node = dict()
for node in G.nodes():
    degree_of_node[node] = len(G[node])

degree_cdf = Cdf(degree_of_node.values())
thinkplot.Cdf(degree_cdf)
thinkplot.show()

# for degree in range(degree_of_node.values().max(), 0, -1):

# print(nodes.info())
# print()
# print(edges.info())
