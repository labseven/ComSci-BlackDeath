import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import thinkplot
import thinkstats2
from thinkstats2 import Cdf, Pmf

from import_owtrad import import_owtrad

max_steps = 100000




# Import the OWTRAD dataset
nodes, edges = import_owtrad()


# Select the edges that we want to use
edges_to_use = edges.loc[(edges.USES == 'trd') | (edges.USES == 'plg')]
edges_list = zip(edges_to_use['NODE1'], edges_to_use['NODE2'])

# Make nx graph
G = nx.Graph()
G.add_edges_from(edges_list)


print("G Len nodes:", len(G.nodes()))
print("G Len edges:", len(G.edges()))





# Build  networks
trade_edges = edges[edges['USES'] == 'trd']
pilgrimadge_edges = edges[edges['USES'] == 'plg']
print("Trade routes:", len(trade_edges))
print("Pilgrimadge routes:", len(pilgrimadge_edges))
print()

network_trade = nx.Graph()
network_trade.add_edges_from(zip(trade_edges.NODEID1, trade_edges.NODEID2))

network_pilgrimadge = nx.Graph()
network_pilgrimadge.add_edges_from(zip(pilgrimadge_edges.NODEID1, pilgrimadge_edges.NODEID2))


print("Trade nodes:", len(network_trade.nodes()))
print("Pilgrimadge nodes:", len(network_pilgrimadge.nodes()))


def draw_graph(G):
    nx.draw_circular(G,
                     node_size=100,
                     with_labels=True)
    plt.show()

# (SLOW for large graphs)
# draw_graph(G)


# # Init DataFrame
# node_df = pd.DataFrame(columns=["nodes", "susceptible", "infected", "dead"])
# node_df.nodes = G.nodes()
# node_df.susceptible = [100]*len(G.nodes())
# node_df.infected = [0]*len(G.nodes())
# node_df.dead = [0]*len(G.nodes())



# cur_infected holds all the cities that are currently infected
# It is seeded with the starting cities


class CityInfectionModel:
    """ Tracks intra-city SIR models, and inter-city infection transmission rates """
    S = 0
    I = 1
    D = 2

    infection_rate = .2
    mortality_rate = .2
    transmission_rate = .3

    def __init__(self, nodes, max_steps):
        self.node_list = list(nodes)
        self.cur_infected = set()

        # Make np array to hold entire history
        # 3D: axis0 = node; axis1=s,i,d; axis2=history
        self.history = np.zeros((len(self.node_list), 3, max_steps), dtype=np.int32)
        # Init susceptible @ time 0 to 100
        self.history[:, 0, 0] = 100

    def cityI(self, city):
        return self.node_list.index(city)

    def city_make_infected(self, city, time_step, num_infected):
        # Remove population from susceptible to infected
        self.history[self.cityI(city), self.S, time_step] -= num_infected
        self.history[self.cityI(city), self.I, time_step] += num_infected

    def city_make_dead(self, city, time_step, num_dead):
        self.history[self.cityI(city), self.I, time_step] -= num_dead
        self.history[self.cityI(city), self.D, time_step] += num_dead

    def city_make_susceptible(self, city, time_step):
        self.history[self.cityI(city), self.S, time_step] = self.history[self.cityI(city), self.S, time_step - 1]

    def SIR_step_one_city(self, city, time_step):
        cur_susceptible, cur_infected, cur_dead = self.history[self.cityI(city), :, time_step]
        print(cur_susceptible, cur_infected, cur_dead)

        num_to_infect = (cur_infected/cur_susceptible) * infection_rate
        num_to_die = cur_infected * mortality_rate

        self.city_make_susceptible(city, time_step + 1)
        self.city_make_infected(city, time_step + 1, num_to_infect)
        self.city_make_dead(city, time_step + 1, num_to_die)

    def SIR_step(self, time_step):
        for city in cur_infected:
            self.SIR_step_one_city(city, time_step)

    def transmit_intercity(self, node1, node2, time_step):
        city_make_infected(neighbor, time_step, 1)

    def intercity_step_one_city(self, city, time_step):
        p_transmission = transmission_rate * self.history[self.cityI(city), self.I, time_step]
        for neighbor in G[city]:
            if toss(p_transmission):
                self.transmit_intercity(city, neighbor)



plague = CityInfectionModel(G.nodes(), max_steps)
time_step = 0
init_infected = ["Paris"]

# Init infection
for city in init_infected:
    plague.city_make_infected(city, 0, 10)

print(plague.history[0,0,0])
print(plague.history[plague.history[:,0,0] != 100])
print(plague.history[plague.cityI("Paris")])



# Init i and infected_timestamps
i = 0
for city in cur_infected:
    infected_timestamps[city] = infected_timestamps[city].union(set([i]))
    infect_city(node_df, city, 3, 0)


def toss(p):
    return np.random.ranf() < p


# At each step, neighbors of cur_infected have a p chance of being infected
def step_infect(G, cur_infected, p):
    newly_infected = set()
    for infected_city in cur_infected:
        neighbors = G[infected_city]
        for city in neighbors:
            if toss(p):
                newly_infected.add(city)
    return newly_infected

# Tracking the number of times the disease spreads
infections_count = 0
# Probability of disease transmission
p = .1


# Run the simulation
while (infections_count < 6 * len(G.nodes())):
    newly_infected = step_infect(G, cur_infected, p)

    for city in newly_infected:
        cur_infected.add(city)
    infections_count += len(newly_infected)

    for city in newly_infected:
        infected_timestamps[city] = infected_timestamps[city].union(set([i]))

    i+=1


# Analytics
print(len(cur_infected))
# print([(city, infected_times[city]) for city in infected_times if infected_times[city]])


# Sum the number of times each city has been infected
infections_per_city = dict()
for city in infected_timestamps:
    infections_per_city[city] = len(infected_timestamps[city])


# infection_cdf = Cdf(infection_count.values())
# thinkplot.Cdf(infection_cdf)
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
