import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random
import sys
import numpy as np
from UnionFind import UnionFind
from UnionNode import UnionNode
np.set_printoptions(threshold=sys.maxsize)

def solve():
    size = 50
    H = 25
    print("dog")
    G=nx.MultiGraph()
    G.add_nodes_from([i for i in range(size)])
    # Add the nodes to the graph
    homes = set()
    while H>0 :
        value = random.randint(0, size-1)
        while value in homes:
            value = random.randint(0, size-1)
        homes.add(value)
        H-=1

    print([str(i) for i in range(50)])
    print(homes)
    un = UnionFind()
    source = UnionNode(0)
    print(type(source.get_vertices()))
    dict = source.vertices
    unIndex = 0
    unIndex+=1
    dict[0] = unIndex
    # union find index of the elements array
    un.add(source)




    for a in homes:
        # print(a)
        loc = UnionNode(a)
        dict = loc.get_vertices()
        dict[a] = unIndex
        unIndex+=1
        un.add(loc)
    # print(un)



    G.add_node(0);

    weigh = 1
    prev = np.array([0, 0, 0, 0, 0, 0, 0])
    i = 1
    while i < size :
        j = 0
        while j < 7:
            G.add_node(i+j)
            G.add_edge(i+j, prev[j], weight=weigh )
            j+=1
        j = 0
        weigh+=1
        while j < 6:
            if(j == 0):
                G.add_edge(i+j, i+j+6, weight=1 )
            G.add_edge(i+j, i+j+1, weight=1 )
            j+=1
        j = 0
        while j < 7:
            prev[j] = i+j
            j+=1
        i+=7
    # nx.draw(G)
    # # nx.draw_spectral(G)
    # plt.show()
    # A = nx.adjacency_matrix(G)
    A = nx.to_numpy_matrix(G, nodelist=[i for i in range(size)])
    print(A)

solve()
