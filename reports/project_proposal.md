# Modeling Black Death:
##### Adam Novotny and Apurva Raman
We intend to model the epidemic known as Black Death. Using datasets from the Old World Trade Routes (OWTRAD) project, we will recreate a network of historically correct cities and trade routes, and then analyze the spread of disease through this network. We are interested analyzing transmission temporally, and seeing how initial parameters affect the results. We are interested in this project because of its specificity in trying to model a very specific scenario, and we want to see how generalizing the model would affect the conclusions (Is the complexity of 'real data' necessary, or only there to tell a good story?).


Bibliography:
Gómez, J. M. and Verdú, M. Network theory may explain the vulnerability of medieval human settlements to the Black Death pandemic. Sci. Rep. 7, 43467; doi: 10.1038/srep43467 (2017).

Gómez et. al. use the Old World Trade Routes Dataset to construct a network model of Black Death transmission in human settlements at the time to determine what settlements were affected most by the pandemic. They use simulation and study the properties of the network from the dataset and use the results to observe infection patterns. They found that reinfection of central cities was instrumental in perpetuating the destruction of the plague. The summary data for each city is included in the supplementary information.

Pastor-Satorras, R., & Vespignani, A. (2002). Immunization of complex networks. Physical Review E, 65(3), 036104.

Pastor-Satorras and Vespignani modeled disease spread over multiple networks. They show that a uniform random immunization strategy is not very efficient, and propose and analyze improved strategies for immunization. They found that scale-free networks are highly susceptible to epidemics, but discovered extremely effective strategies of immunization for it. They suggest that their model is relevant to the spreading of viruses over the internet, and propose a way to extend it to model STD transmission.

Keeling, M. J., & Eames, K. T. . (2005). Networks and epidemic models. Journal of the Royal Society Interface, 2(4), 295–307. 10.1098/rsif.2005.0051

The authors provide an overview of the analogies between network attributes and epidemic characteristics. Rather than conducting a specific experiment, they explain the value of various models in simulating disease transmission. For example, they recommend scale-free networks constructed as described by Barabasi & Albert for creating models that account for super-spreaders. 

## Replicate experiment:
We plan on recreating the model presented by Gómez et. al. in "Network theory may explain the vulnerability of medieval human settlements to the Black Death pandemic." They created a realistic network of the Western world, and drew conclusions between city mortality and their network attributes. They used historical data to confirm their model is reasonably accurate simulation of the epidemic, and then discussed the specific characteristics of cities vs their location in the network.

## Extensions:
We are interested in generalizing/simplifying the model (Making a WS model with similar attributes), while trying to preserve the same behavior. Specifically, we are interested in the paper's conclusions about the reinfection of central nodes being a key part in the strength of the epidemic. We want to see how removing these nodes after infection (Death or Immunity) would change the spread of disease.
We are also considering adding "quarantine" to the model, temporally removing nodes or edges, and seeing how transmission is affected.
Two simple additions that were left out of the original paper is assigning 'distance' on edges, and making city infection a float instead of a binary.

Essentially, is the current model a reasonable approximation of the real world, does adding (possibly important) attributes, or is it needlessly complicated already?


## Interpreting Results:
We will analyze the same relationships that the original paper discussed, namely Mortality vs Network Attributes, Network Attributes vs Reinfection Rate. The network attributes they studied were degree, closeness, and clustering. We will hopefully modify the model while preserving the same looking graphs as the original paper.

We expect the Susceptible - Infected - Immune model to need a much higher transmission rate to create an epidemic. By removing the possibility of reinfection, central nodes will not be able to propagate the disease as long, which might create smaller epidemics.

## Concerns:
Importing and parsing the OWTRAD dataset into our model will take some time, and we are unsure if we will be able to generate a stochastic model with similar attributes.
Modeling epidemics takes a lot of domain knowledge, and we are concerned that we won't make an acceptable model by making wrong assumptions.

## Next Steps:
Importing and parsing the OWTRAD dataset is our first big hurdle. We will collect the data into CSVs individually, and then write the parsing together. Then we will figure out how to delegate the simulation work.
At the end of the week, we hope that we will have a functional recreation of the paper's model, so that we can focus on extensions in the second week.
We will also both read about SIS models, and try to get a more general understanding of disease modeling. We will also read a primer on the black death.
