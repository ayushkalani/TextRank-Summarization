import nltk
import itertools
from operator import itemgetter
import networkx as nx
import os
from summa import summarizer
import matplotlib.pyplot as plt
from networkx.drawing.nx_pylab import draw_networkx
def lDistance(firstString, secondString):
    "Function to find the Levenshtein distance between two words/sentences - gotten from http://rosettacode.org/wiki/Levenshtein_distance#Python"
    if len(firstString) > len(secondString):
        firstString, secondString = secondString, firstString
    distances = range(len(firstString) + 1)
    for index2, char2 in enumerate(secondString):
        newDistances = [index2 + 1]
        for index1, char1 in enumerate(firstString):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1], distances[index1 + 1], newDistances[-1])))
        distances = newDistances
    return distances[-1]
def buildGraph(nodes):
    "nodes - list of hashables that represents the nodes of the graph"
    # itertools generate all possible combinations ex {1,2,3} itertools.combinations(array,2)=1,2 1,3 2,3
    gr = nx.Graph()  # initialize an undirected graph
    gr.add_nodes_from(nodes)
    nodePairs = list(itertools.combinations(nodes, 2))
    # add edges to the graph (weighted by Levenshtein distance)
    for pair in nodePairs:
        firstString = pair[0]
        secondString = pair[1]
        levDistance = lDistance(firstString, secondString)
        gr.add_edge(firstString, secondString, weight=levDistance)
    

    return gr
def buildGraphfors(snodes):
    graphi=nx.Graph()
    graphi.add_nodes_from(snodes)
    nodepar=list(itertools.combinations(snodes,2))
    
    
    return graphi
    
    

def extractSentences(text):
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sentenceTokens = sent_detector.tokenize(text.strip())
    print sentenceTokens
    graph = buildGraphfors(sentenceTokens)

    calculated_page_rank = nx.pagerank(graph, weight='weight')
    # print calculated_page_rank
    # most important sentences in ascending order of importance
    sentences = sorted(calculated_page_rank, key=calculated_page_rank.get, reverse=True)
    
    # return a 100 word summary
    summary = ' '.join(sentences)
    summaryWords = summary.split()
    summaryWords = summaryWords[0:101]
    summary = ' '.join(summaryWords)
    
    return summary


def drawgraph(G, labels):
    # labels = labels.items()
    # labels=[(v, k) for k, v in labels.iteritems()]
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=500, alpha=0.8)
    nx.draw_networkx_edges(G, pos, arrows=True)
    # nx.draw_networkx_labels(G,pos,labels,font_size=10)
    # nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
    plt.show()
    
text = """ Development of the website using Bootstrap , JavaScript , jQuery , Ajax and HTML5/CSS . Configuring the Facebook OAuth login for website and setting up of the payments from CCAvenue and configuring automated SMS alerts along with SEO.I am a problem solver, willing to learn new tools and solving problems in software and consultancy industries.I want to apply my knowledge in computer science to solve problems and develop business based solutions for the organisation.I am confident that I could make a positive impact on the community.
"""
text1 = """ The earthquake that struck northern Iran brought
reminders of another quake that devastated Soviet Armenia in 1988.
   Like Thursday's earthquake in Iran, the Dec. 7, 1988, earthquake
in Armenia killed about 25,000 people. Most died in structures that
collapsed when the quake hit.
   ``It's very similar to what we had in Armenia,'' said Russ
Needham, a geophysicist with the U.S. Geological Survey.
   The Armenian quake was measured at 6.9 on the Richter scale, but
Thursday's earthquake shook the earth with a magnitude of 7.7
according to the U.S. Geological Survey.
   In the Iranian quake, the casualty count was pushed up by the
fact that people were indoors and asleep at the time, just after
midnight. Many of the victims lived in fragile homes built of a
ceramic-type brick or adobe that collapses easily.
   In the Armenian quake, a Soviet parliamentary report later
blamed the high number of fatalities on shoddily built buildings.
   ``Most casualties from earthquakes are caused by something
falling on top of you,'' said Needham in a telephone interview from
Golden, Colo.
   The quake struck an area of Iran where most of the buildings are
built on a flood plain of loosely deposited soil that shifts in an
earthquake and allows structures to collapse, Needham said.
   The 7.7-magnitude quake was the largest ever recorded in that
area, where two major plates of the earth's crust meet, he said.
   ``Iran is in a very active seismic region,'' he said, and that
there have been many smaller quakes.
   Twelve earthquakes greater than magnitude 7 have occurred in
Iran during the last 30 years, Needham said.
   A quake of magnitude 7 is considered a major earthquake, capable
of widespread, heavy damage in populated areas."""
print extractSentences(text)

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
sentenceTokens = sent_detector.tokenize(text.strip())
graph = buildGraph(sentenceTokens)
#drawgraph(graph, sentenceTokens)
