import numpy as np
import matplotlib.pyplot as plt
import graph_AL as graph
import dsf
import min_heap
from scipy.interpolate import interp1d
               
                        
def kruskal(G,trace=False):
    weight_heap = min_heap.MinHeap() # Used to find lowest cost edge
    S = dsf.DSF(len(G.al))           # Used to determine if two vertices are already connected
    mst = graph.Graph(len(G.al),weighted=True)  # Used to store solution 
    count = 0        # Used to keep track of edges added to MST     
    # Your code goes here
    
    for i in range(len(G.al)):
        for j in G.al[i]:
            found = False
            for k in weight_heap.heap:
                if k.data[-1] == i and k.data[0] == j.dest:
                    found = True
            if G.directed or not found:
                weight_heap.insert(min_heap.HeapRecord(j.weight,[i,j.dest]))

    while count < len(G.al)-1 and len(weight_heap.heap)>0:
        e = weight_heap.extractMin()
        if S.find(e.data[0]) != S.find(e.data[-1]) or S.find(e.data[0]) == -1:
            count += 1
            mst.insert_edge(e.data[0],e.data[-1],e.key)
            S.union(e.data[0],e.data[-1])
            if trace:
                print('edge: (',e.data[0],',',e.data[1],',',e.key,')')
                print('edge does not create a cycle, thus it is added to MST')
                mst.draw()
                print()
        else:
            if trace:
                print('edge: (',e.data[0],' ',e.data[-1],' ',e.key,')')
                print('edge creates a cycle, thus it is NOT added to MST')
                mst.draw()
                print()         
    if count == len(G.al)-1:
        return mst
    return None

def prim(G,origin=0, trace=False):
    weight_heap = min_heap.MinHeap()  # Used to find lowest cost edge  
    mst = graph.Graph(len(G.al),weighted=True)  # Used to store solution 
    count = 0        # Used to keep track of edges added to MST   
    C = [origin]

    for u in G.al[origin]:
        weight_heap.insert(min_heap.HeapRecord(u.weight,[origin,u.dest]))

    for i in range(len(G.al)-1):
        e = weight_heap.extractMin()
        while e.data[-1] in C:
            e = weight_heap.extractMin()

        for u in G.al[e.data[-1]]:
            if u.dest not in C:
                weight_heap.insert(min_heap.HeapRecord(u.weight,[e.data[-1],u.dest]))
        
        if e.data[-1] not in C:
            count += 1
            mst.insert_edge(e.data[0],e.data[-1],e.key)
            C += [e.data[-1]]
            if trace:
                print('i: ', i)
                print('(u,v,w): (',e.data[0],',',e.data[1],',',e.key,')')
                print('C: ', C)
                mst.draw()
                print()
    if count == len(G.al)-1:
        return mst
    return None

if __name__ == "__main__":   
    plt.close("all")   
    
    g = graph.Graph(7,weighted=True)
    g.insert_edge(0,1,8)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.insert_edge(4,6,9)
    g.insert_edge(5,6,10)
    g.insert_edge(4,5,6)
    g.insert_edge(3,6,7)
    g.display()
    g.draw('Original graph')
    
    # g = graph.Graph(6,weighted=True)
    # g.insert_edge(0,1,9)
    # g.insert_edge(0,3,13)
    # g.insert_edge(1,2,2)
    # g.insert_edge(1,3,6)
    # g.insert_edge(1,4,3)
    # g.insert_edge(2,4,1)
    # g.insert_edge(3,4,5)
    # g.insert_edge(3,5,4)
    # g.insert_edge(4,5,7)
    # g.display()
    # g.draw('Original graph')
    
    print('Kruskal')
    mst = kruskal(g)
    if mst!=None:
        mst.draw('Kruskal')
        
    print('Prim')
    mst = prim(g)
    if mst!=None:
        mst.draw('Prim')
        

