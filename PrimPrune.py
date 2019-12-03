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

def PrimPrune(un, G,locs):
    soln = UnionPrim(un, G, locs)

     # create the MST as a MultiGraph
     # DFS and prune paths that do not hit any homes
     # record locations of union leaves drop off nodes
        # if dfs(v) returns a list mark curr v as drop loc for home that is a leaf
