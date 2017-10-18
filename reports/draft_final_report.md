# Modeling Mortality and Transmission of the Black Plague
Adam Novotny, Apurva Raman

## Abstract:
Gómez and Verdú model the infection patterns of the Black Death pandemic in their 2017 paper “Network theory may explain the vulnerability of medieval human settlements to the Black Death pandemic”. They construct a historically accurate network representing Europe and part of Asia and Africa using the [OWTRAD (Old World Trade Routes) dataset][1], which contains information about medieval cities and the trade and pilgrimage routes between them. They find that hub cities are prone to being reinfected more often. We replicate this experiment and add an SIR model in each city to investigate how mortality affects transmission of the disease through the network. We find TODO: result here (the disease to spreads through the network and total mortality is affected by x, y, z).

## Replication
Gómez and Verdú construct a historically accurate network representing Europe and part of Asia and Africa using the OWTRAD (Old World Trade Routes) dataset, which contains information about medieval cities and the trade and pilgrimage routes between them. They start the plague in a city in Asia, representing a city’s infection state as a binary state, and then let the plague propagate through the network with a given transmission chance. In their model, hub cities get reinfected repeatedly. They find that cities with high mortality (as reported in historical accounts) were cities with high centrality on the network. From this, they conclude that reinfection from neighboring cities is a possible mechanism for higher mortality rates.

![Figure 1: network](media/Geographical_network.png)
Figure 1: A geographical representation of the network. Created by Gómez and Verdú.

We attempt to replicate the network from the datasets that Gómez and Verdú list in their supplement. Our network is different, particularly with respect the number of nodes and mean degree. We have 259 extra nodes present in our network, which indicates that our data is different despite being created from the same files. As they manually craft their dataset from 23 files, we cannot identify where the mismatch occurs.

#### Table of network characteristics (vs Gómez and Verdú):
| Characteristic | Our Network’s Value | Reported Value |
| --- | --- | --- |
| Number of Nodes | 1570 | 1311
| Number of Edges | 2069 | 2084
| Mean Degree | 2.63 | 3.18
| Mean Degree Trade | 2.05 | 2.49
| Mean Degree Pilgrimage| 0.59 |  0.69
| Transitivity | 0.065 | 0.098 |


## Modeling Mortality
Their model simulates transmission between each city, but does not simulate a city’s population becoming infected or dying. Gómez and Verdú suggest that there may be some relationship between reinfection and mortality, but do not model mortality directly. Thus, from the Gómez and Verdú model, it is unclear whether mortality changes the pattern of infection through the network and whether their conclusions hold when mortality is added to the model.

To determine whether hubs still get reinfected more frequently when we add mortality to the simulation, we extend the model to simulate mortality by adding an SIR model to each city.

An SIR model is an epidemiological model for determining the number of people infected with a disease in a well mixed population. It has three states. The first is the susceptible state, which represents the number of people who are not infected, but could become infected. At each timestep, susceptible people have a probability of transitioning to the infected state, which is determined by the amount of infected people in the population and the rate of infection. In a traditional SIR model, infected people have a probability of recovering and becoming immune (the third state) at each timestep, but we use this third state to track the number of dead from the disease, which uses the mortality rate instead of the recovery rate.

We added a state, "not yet susceptible" before susceptible. A percentage of the population in NYS gets moved to S every time a city gets infected from a neighbor. This model prevents a single infection from wiping out the entire city, This reflects historical accounts of an epidemic, ... {new strains and resistance to old strains}.

We give each city a population of 250 at the start of the simulation. At each timestep, the tally of NYS, susceptible, infected, and dead residents is updated based on their respective probabilities and the number of infected people and the number of infections in each timestep.

```
Code block of the 4 diff eq's
```

A city with infected residents may also transmit the disease to another city with a probability determined by transmission rate and the number of infected citizens.

```
Diff eq
```

Cities can transmit disease to cities that are already infected, which are the reinfection events that Gómez and Verdú track.

We run the simulation of infection to identify if a relationship between hub cities and amount of reinfection is present.

![Figure 2: degree_vs_reinfection](media/degree_vs_infections2.png)
Figure 2: Reinfections vs Degree Centrality

Figure 2 shows the relationship between degree centrality (the fraction of nodes it is connected to) and number of reinfections.  Reinfections appear to increase proportionally with degree centrality.

Degree centrality is directly proportional to degree, and is one of the methods Gómez and Verdú use to determine whether a city is a hub. Despite the differences between the networks and the addition of the SIR modeling of mortality, Figure 2 shows that hub cities get reinfected more often in our model as well.


![Figure 3: SIR_One_city.png](media/SIR_One_city.png)
Figure 3: SIR in Europe

We plot the sum of the SIR metrics in the network given an infection rate of 0.1, a mortality rate of 0.1, and a transmission rate of 0.05.

The number of susceptible residents decreases as infected residents increases, and infection slows down as more people die. The death rate slows when about half of the population dies.

This indicates the SIR model is working as expected; the population transitions from state to state, and when mortality and infection rates are equal, mortality is limiting transmission.

![Figure 4: Sum Reinfections CDF](media/Sum_Reinfections_CDF.png)
Figure 4: Sum of Reinfections CDF

Figure 4 shows the distribution of the number of reinfections. There is a steep jump around 1500 reinfections per city (about 60% of cities are reinfected about 1500 times), which is something we are investigating.

Our next step is to sweep the three parameters, and analyze the data we extract from that.


## References

[1]: http://ciolek.com/OWTRAD/DATA/oddda.html  "OWTRAD Dataset"

**Gómez, J. M. and Verdú, M.** "Network theory may explain the vulnerability of medieval human settlements to the Black Death pandemic." *Sci. Rep. 7*, 43467; doi: 10.1038/srep43467 (2017).

Gómez et. al. use the Old World Trade Routes Dataset to construct a network model of Black Death transmission in human settlements at the time to determine what settlements were affected most by the pandemic. They use simulation and study the properties of the network from the dataset and use the results to observe infection patterns. They found that reinfection of central cities was instrumental in perpetuating the destruction of the plague. The summary data for each city is included in the supplementary information.

**Pastor-Satorras, R., & Vespignani, A.** "Immunization of complex networks." *Physical Review* E, 65(3), 036104 (2002).

Pastor-Satorras and Vespignani modeled disease spread over multiple networks. They show that a uniform random immunization strategy is not very efficient, and propose and analyze improved strategies for immunization. They found that scale-free networks are highly susceptible to epidemics, but discovered extremely effective strategies of immunization for it. They suggest that their model is relevant to the spreading of viruses over the internet, and propose a way to extend it to model STD transmission.

**Keeling, M. J., & Eames, K. T.** "Networks and epidemic models." *Journal of the Royal Society Interface*, 2(4), 295–307. 10.1098/rsif.2005.0051 (2005).

The authors provide an overview of the analogies between network attributes and epidemic characteristics. Rather than conducting a specific experiment, they explain the value of various models in simulating disease transmission. For example, they recommend scale-free networks constructed as described by Barabasi & Albert for creating models that account for super-spreaders.
