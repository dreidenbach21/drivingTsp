import networkx as nx
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
import random
import sys
import numpy as np
from UnionFind import UnionFind
from UnionNode import UnionNode
from UnionPrim import UnionPrim
np.set_printoptions(threshold=sys.maxsize)

def UnionPrimTest():
    G=nx.MultiGraph()
    G.add_nodes_from([0,1,2,3])
    G.add_weighted_edges_from([(0,1,2),(0,2,1),(1,3,3),(2,3,2)])
    locs = {}
    locs[0] = 0
    locs[3] = 1

    un = UnionFind()

    source = UnionNode(0)
    dict = source.get_vertices()
    dict[0] = 0
    un.add(source)

    home = UnionNode(3)
    dict2 = home.get_vertices()
    dict2[3] = 3
    un.add(home)

    vert_edges_MST = UnionPrim(un, G,locs)
    print(vert_edges_MST)
UnionPrimTest()
