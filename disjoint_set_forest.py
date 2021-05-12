import numpy as np
import matplotlib.pyplot as plt
import graph_AL as graph
import dsf

def connected_components(G,trace=False):
    # Returns the disjoint set forest representing the connected components of G
    S = dsf.DSF(len(G.al))
    for u in range(len(G.al)):
        for v in G.al[u]:
            if trace:
                s = S.set_list()
                print('Disjoint set forest:',S.parent)
                print('Number of connected components:',len(s))
                print('Connected components:',s)
                S.draw()
                print()
            S.union(u,v.dest)
    return S

if __name__ == "__main__":   
    plt.close("all")   
    print('Graph 1')
    G =graph.Graph(8)
    G.insert_edge(0,2)
    G.insert_edge(0,3)
    G.insert_edge(1,3)
    G.insert_edge(1,4)
    G.insert_edge(2,3)
    G.insert_edge(3,4)
    G.insert_edge(5,6)
    
    G.display()
    G.draw()

    S = connected_components(G)
    s = S.set_list()
    print('Disjoint set forest:',S.parent)
    print('Number of connected components:',len(s))
    print('Connected components:',s)
    S.draw()
    
    print('Graph 2')
    G =graph.Graph(8)
    G.insert_edge(0,2)
    G.insert_edge(0,3)
    G.insert_edge(1,5)
    G.insert_edge(2,3)
    G.insert_edge(3,4)
    G.insert_edge(5,6)
    
    G.display()
    G.draw()

    S = connected_components(G,trace=True)
    s = S.set_list()
    print('Disjoint set forest:',S.parent)
    print('Number of connected components:',len(s))
    print('Connected components:',s)
    S.draw()
    
'''
Program output:    
Graph 1
Graph representation
directed: False, weighted: False
Adjacency list:
al[0]=[2, 3]
al[1]=[3, 4]
al[2]=[0, 3]
al[3]=[0, 1, 2, 4]
al[4]=[1, 3]
al[5]=[6]
al[6]=[5]
al[7]=[]
Disjoint set forest: [-1, 0, 0, 0, 0, -1, 5, -1]
Number of connected components: 3
Connected components: [[0, 1, 2, 3, 4], [5, 6], [7]]
Graph 2
Graph representation
directed: False, weighted: False
Adjacency list:
al[0]=[2, 3]
al[1]=[5]
al[2]=[0, 3]
al[3]=[0, 2, 4]
al[4]=[3]
al[5]=[1, 6]
al[6]=[5]
al[7]=[]
Disjoint set forest: [-1, -1, 0, 0, 0, 1, 1, -1]
Number of connected components: 3
Connected components: [[0, 2, 3, 4], [1, 5, 6], [7]]

'''
