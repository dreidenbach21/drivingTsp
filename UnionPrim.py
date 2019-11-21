import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random
import sys
import numpy as np
from UnionFind import UnionFind
from UnionNode import UnionNode

def UnionPrim(un, G,locs):
    # 1)Create a set mstSet that keeps track of vertices already included in MST.
    edges = set()
    vertices = set()
    # 2) Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE. Assign key value as 0 for the first vertex so that it is picked first.
    while(un.n_comps > 1):
        for loc : locs:
            neigh = G.neighbors(loc)


    # 3) While mstSet doesn’t include all vertices
        # ….a) Pick a vertex u which is not there in mstSet and has minimum key value.
        # ….b) Include u to mstSet.
        # ….c) Update key value of all adjacent vertices of u. To update the key values, iterate through all adjacent vertices. For every adjacent vertex v, if weight of edge u-v is less than the previous key value of v, update the key value as weight of u-v
