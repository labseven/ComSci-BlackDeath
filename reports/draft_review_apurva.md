## Review of "How Attached Are We to Preferential Attachment?" by Erica Lee and Emily Yeh

###### Apurva Raman

___

#### Question:  What is your understanding of the experiment the team is replicating?  What question does it answer?  How clear is the team's explanation?

I don't know what the Holme Kim algorithm is or how they construct the graph.

Question 1: Can we use the method used by Holme and Kim to generate graphs with higher clustering than BA, and are these graphs better models of social networks?

Question 2: How can the the Holme Kim method be modified so that it is produces similar results for directed graphs?

The presentation of the results is pretty clear, but the methodology isn't clear yet.


#### Methodology: Do you understand the methodology?  Does it make sense for the question?  Are there limitations you see that the team did not address?

It's unclear how you are constructing the graph (what part of the process is different from BA? How is that done?) How did you implement the Holme Kim algorithm?


#### Results: Do you understand what the results are (not yet considering their interpretation)?  If they are presented graphically, are the visualizations effective?  Do all figures have labels on the axes and captions?

Stating what PMFs being linear means would probably be helpful here, and consider seeing if the CDFs give you more useful information about the shape of the distribution.

#### Interpretation: Does the draft report interpret the results as an answer to the motivating question?  Does the argument hold water?

There isn't much interpretation here yet for replication, which makes sense given where you are.
However, you could do some interpretation of the results from replication at this point. Talking about whether you expected power law and what the less linear tail means on the Facebook data and what could have caused it may be a good start.

#### Replication: Are the results in the report consistent with the results from the original paper?

Your replication appears to be sound for the Facebook data, but does not seem to hold for these results:
|              | Holme Kim | Holme Kim Expected |
| ---          | ---       | ---                |
| Clustering   | 0.082     | 0.037              |
| Mean Degrees | 85.274    | 43.7               |

If you could explain these differences or if you have a conjecture about why they are different, that would be helpful. Acknowledging this difference or explaining why it is or isn't important if there isn't a clear explanation would be a good start.

I'm not sure what the degrees count means either. Is this the sum of the degree of each node?

#### Extension: Does the report explain an extension to the original experiment clearly?  Is it a sensible extension in the sense that it has the potential to answer an interesting question that the original experiment did not answer?

I understand that the extension is making the Holme Kim model applicable to directed graphs for the purposes of better modeling social networks. This approach makes sense, and I think it's answering the following question: How can Holme Kim be made to have the same properties for directed graphs?

In the case that this is the question, I think I need a better understanding of exactly what you're changing to make it work for directed graphs- I think it has something to do with with preferential attachment, but at this point, it's unclear to me.

#### Progress: Is the team roughly where they should be at this point, with a replication that is substantially complete and an extension that is clearly defined and either complete or nearly so?

It looks like you are where you need to be. You've done the replication successfully and are working on your extension.

#### Presentation: Is the report written in clear, concise, correct language?  Is it consistent with the audience and goals of the report?  Does it violate any of the recommendations in my style guide?

The language you're using is good, but it could be more concise (e.g. "We investigate an extension" vs "We extend").

#### Mechanics: Is the report in the right directory with the right file name?  Is it formatted professionally in Markdown?  Does it include a meaningful title and the full names of the authors?  Is the bibliography in an acceptable style?

Looks good!

- Report is in the correct directory, has the correct filename
- Looks professionally formatted, consider figure titles and captions
- Names were missing, but you fixed that
- Bibliography is in an acceptable style
