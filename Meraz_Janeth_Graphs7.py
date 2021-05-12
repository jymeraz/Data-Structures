import numpy as np
import matplotlib.pyplot as plt
import graph_AL as graph

def in_degrees(G):
    L = [0 for i in range(len(G.al))]
    for vert in G.al:
        for edge in vert:
            L[edge.dest] +=1
    return L

def topological_sort(G,trace=False):
    in_deg = in_degrees(G)
    Q = [in_deg[in_deg==0]]
    T = []
    while Q != []:
        v = Q.pop(0)
        T += [v]
        for u in G.al[v]:
            in_deg[u.dest] = in_deg[u.dest] - 1
            if in_deg[u.dest] == 0:
                Q += [u.dest]
        if trace:
            print('v: ', v)
            print('T: ', T)
            print('in_degrees: ', in_deg)
            print('Q: ', Q)
            print()
    if len(T) == len(G.al):
        return T
    return None
                
if __name__ == "__main__":   
    plt.close("all")  
    
    print('=== Graph 1 ===')
    G =graph.Graph(9,directed = True)
    G.insert_edge(0,1)
    G.insert_edge(0,4)
    G.insert_edge(1,2)
    G.insert_edge(1,5)
    G.insert_edge(2,3)
    G.insert_edge(4,1)
    G.insert_edge(4,5)
    G.insert_edge(4,7)
    G.insert_edge(5,2)
    G.insert_edge(5,6)
    G.insert_edge(5,8)
    G.insert_edge(6,2)
    G.insert_edge(6,3)
    G.insert_edge(7,5)
    G.insert_edge(7,8)
    G.insert_edge(8,6)
    G.draw(' ')
    s = topological_sort(G)
    print(s)
   
    print('===Graph 2 ===')
    G =graph.Graph(9)
    G.insert_edge(0,1)
    G.insert_edge(0,4)
    G.insert_edge(1,2)
    G.insert_edge(3,2)
    G.insert_edge(4,1)
    G.insert_edge(4,5)
    G.insert_edge(4,7)
    G.insert_edge(5,1)
    G.insert_edge(5,2)
    G.insert_edge(5,6)
    G.insert_edge(5,8)
    G.insert_edge(6,2)
    G.insert_edge(6,3)
    G.insert_edge(7,5)
    G.insert_edge(7,8)
    G.insert_edge(8,6)
    G.draw(' ')
    s = topological_sort(G,trace=True)
    print(s)
   
