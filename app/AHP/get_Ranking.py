import networkx as nx
import numpy as np
import json

def get_Centrality(filepath, DiGraph = False, Weighted = False):
    
    # filename += ".csv"
    data = open(filepath, 'rb')
    #make a Graph
    if DiGraph:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    
    if Weighted:
        G = nx.read_weighted_edgelist(data,delimiter=',',create_using=G)    
    else:
        G = nx.read_edgelist(data,delimiter=',',create_using=G)

    #computing the Centrality Measures

    
    DC = nx.degree_centrality(G)
    CC = nx.closeness_centrality(G)
    BC = nx.betweenness_centrality(G)
    if DiGraph:
        G = G.reverse()
    EC = nx.eigenvector_centrality(G,1000)

    return {"DC":DC, "CC":CC, "BC": BC, "EC":EC}

def get_Ranking(csvpath, jsonpath, DiGraph = False, Weighted = False):

    rank = {}
    # print(DiGraph)
    # print(Weighted)
    Centrality = get_Centrality(csvpath,DiGraph,Weighted)
    # print(Centrality)
    with open(jsonpath) as json_file:
        w = json.load(json_file)
        for el in Centrality["DC"]:
            rank[el]=w['w0']*Centrality["DC"][el]+w['w1']*Centrality["CC"][el]+w['w2']*Centrality["BC"][el]+w['w3']*Centrality["EC"][el]

        # print(rank)
    return rank