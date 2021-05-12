"""
Course: CS 2302 
Author: Janeth Meraz
Assignment: Lab 5
Instructor: Olac Fuentes
T.A.: Oscar Galindo
I.A.: Seth Flores
Date of last modification: July 28, 2020
Purpose: Implement graph algorithms in order to solve problems for real life 
    examples using text files as a data source. The graph algorithms include 
    graph dearch algorithms and minimum spanning tree algorithms.        
"""
import graph_AL as graph
import math
import min_heap
import dsf

# Function returns an adjacency list representation of a distance matrix file and a list with the city names.
# The city file is first opened and each city name is appended to a new list.
# A graph is created the length of the city list and the distances matrix file is opened and read.
# Each distance is added to the graph as a weighted edge until the whole file has been traversed. 
def al_representation(distances_file,cities_file):           
    file = open(cities_file,'r')
    line = file.readline().rstrip('\n')
    cities = []
    while line:
        cities += [line]
        line = file.readline().rstrip('\n')
    file.close()
    
    G = graph.Graph(len(cities),weighted=True)
    file = open(distances_file,'r')
    for i in range(len(cities)):
        # Create a list out of each line in the file.
        distances = file.readline().rstrip('\n').split(',')
        for j in range(len(distances)):
            # Only append an edge if a distance exists and if the source is less than the destination. 
            if int(distances[j]) != -1 and i < j:
                G.insert_edge(i,j,int(distances[j]))
    file.close()
    return G,cities

# Function creates a file with the shortest paths from every city to every other city.
# A new file is created and the cities list is traversed.
# The lists of previous values and distances are computed for each word.
# These lists are used to determine the path from the current city to every other city as well as the distance.
# These values are written to the file. 
def shortest_paths(G,cities):
    f = open('Meraz_Janeth_Number2.txt', 'w+')
    f.write('Shortest Path from every City to every other City\n\n')
    for i in range(len(cities)):
        prev, dist = dijkstra(G,i)
        for k in range(len(prev)):
            # Only include paths that do not include the root.
            if prev[k] != -1:
                path = get_path(prev,k,cities)
                f.write('Shortest Path from {} to {}: {}\n'.format(cities[i],cities[k],path))
                f.write('Overall Distance: {}\n\n'.format(dist[k]))
    f.close()          
    print('File created named "Meraz_Janeth_Number2.txt" displaying shortest path from every city to every other city.\n')             

# Function traverses a graph from a specified source and returns a list of the previous indexes of each city and distances.
# A min heap is created in order to extract the minimum weighted edge of the unknown edges. 
# Each neighbor of the current vertex is added if they are not known.
# The indexes of distance and previous are updated once a smallest distance has been found.
# This continues until the min heap is empty.
def dijkstra(G,source):
    known = [False for i in range(len(G.al))]
    prev = [-1 for i in range(len(G.al))]
    dist =[math.inf for i in range(len(G.al))]
    dist_heap = min_heap.MinHeap()
    dist[source] = 0
    dist_heap.insert(min_heap.HeapRecord(dist[source],source))
    while len(dist_heap.heap)>0:
        heap_node = dist_heap.extractMin()
        v = heap_node.data
        if not known[v]:
            known[v] = True
            for edge in G.al[v]:
                u = edge.dest
                
                if not known[u]:
                    w = edge.weight
                    if dist[v]+w < dist[u]:
                        prev[u] = v
                        dist[u] = dist[v]+w
                        dist_heap.insert(min_heap.HeapRecord(dist[u],u))
    return prev, dist

# This function returns the minimum spanning tree of a graph. 
# All of the edges of the graph are first inserted into a min heap.
# The minimum weight edge is extracted from the min heap.
# If the source and destination vertices of the edge are not already in the same set, then the edge is added to the graph.
# This continues until the min heap is empty or the number of inserted edges is one less than the number of vertices.
# If a minimum spanning tree exists, then it is returned. 
def kruskal(G):
    weight_heap = min_heap.MinHeap()
    S = dsf.DSF(len(G.al))
    for v in range(len(G.al)):
        for edge in G.al[v]:
            if v<edge.dest:
                weight_heap.insert(min_heap.HeapRecord(edge.weight,[v,edge.dest,edge.weight]))
    mst = graph.Graph(len(G.al),weighted=True)
    count = 0
    while count<len(G.al)-1 and len(weight_heap.heap)>0:
        next_edge = weight_heap.extractMin().data
        if S.union(next_edge[0],next_edge[1])==1:
            mst.insert_edge(next_edge[0],next_edge[1],next_edge[2])
            count+=1 
    if count == len(G.al)-1:
        return mst
    print('Graph has no minimum spanning tree')
    return None

# Function creates a file with the paths from every city to every other city using a mst.
# A new file is created and the cities list is traversed.
# The lists of previous values and distances are computed for each word.
# These lists are used to determine the path from the current city to every other city as well as the distance.
# The difference in distances between the original graph and the mst are computed.
# These values are written to the file for each path.
def diff_distance(G,mst,cities):
    f = open('Meraz_Janeth_Number4.txt', 'w+')
    f.write('Distance from every City to every other City using MST\n\n')
    for i in range(len(cities)):
        # Run Dijkstra's algorithm with the mst and the original graph to compare the difference in distances. 
        prev_mst, dist_mst = dijkstra(mst,i)
        prev, dist = dijkstra(G,i)
        for k in range(len(prev)):
            if prev[k] != -1:
                path = get_path(prev_mst,k,cities)
                f.write('Path from {} to {}: {}\n'.format(cities[i],cities[k],path))
                f.write('Overall Distance: {}\n'.format(dist_mst[k]))
                f.write('Increase in Distance: {}\n\n'.format(dist_mst[k]-dist[k]))
    f.close()          
    print('File created named "Meraz_Janeth_Number4.txt" displaying distances and routes for minimum spanning tree.\n') 

# Function returns the path of a certain index to its root through recursive calls.
def get_path(prev,v,data_list):
    if prev[v]<0:
        return [data_list[v]]
    return get_path(prev,prev[v],data_list)+[data_list[v]]

# Function creates a graph and displays a path to the goal vertex. 
# The possibilities of states are first created and their length is used to create the graph. 
# The graph's edges are inputted manually between valid states. 
# Breadth first search algorithm is called to create a list of previous indices. 
# The path is computed from the previous list.
# The specific actions of the path are printed.     
def rowboat_problem(experiment=False):
    world_states = binary_list()
    G = graph.Graph(len(world_states))
    G.insert_edge(0,10)
    G.insert_edge(1,11)
    G.insert_edge(1,13)
    G.insert_edge(2,10)
    G.insert_edge(2,11)
    G.insert_edge(2,14)
    G.insert_edge(4,13)
    G.insert_edge(4,14)
    G.insert_edge(5,13)
    G.insert_edge(5,15)
    if experiment:
        G.draw('Rowboat Problem Graph')
        G.display()
        print()
    # Bredth-first search algorithm called.
    prev = bfs(G)
    path = get_path(prev,len(world_states)-1,world_states)
    # Specific actions printed to the console. 
    display_actions(path)

# Function returns a list with indexes that have the index of the element previous to each element.
# The source index is appended to a queue.
# The first element in the queue is dequeued and its edges are queued if they are not visited.
# If they are not visited, then their previous value is set to the current vertex and are not visited.
# Once the queue is empty, the prev list is returned. 
def bfs(G,source=0):
    visited = [False for i in range(len(G.al))]
    prev = [-1 for i in range(len(G.al))]
    visited[source] = True
    Q = [source]
    while len(Q)>0:
        v = Q.pop(0)
        for edge in G.al[v]:
            u = edge.dest
            if not visited[u]:
                visited[u] = True
                prev[u] = v
                Q.append(u)
    return prev

# Function creates a list of all the possibilities of an n-bit number
# The digit 0 is used first and once the recursive call finishes, the digit 1 is then used.
# Once the string reaches the length n, its list is returned and concatenated to the rest of the list. 
# Once all possibilities have been exhausted, the list is returned. 
def binary_list(string_so_far='',digits_left=4):
    L = []
    if digits_left==0:
        return [string_so_far]
    else:
        L += binary_list(string_so_far+'0',digits_left-1)
        L += binary_list(string_so_far+'1',digits_left-1)
    return L

# Function displays specific actions taken in the rowboat problem. 
# The actions are based on the previous state of the world and the current state of the world. 
# The 4-bit strings are evaluated and the action that takes place to transform the string is printed. 
# The actions are printed until the traversal reaches the end of the path.
def display_actions(path):
    print('Sequence of actions that the man must take to cross the river:')
    print('{}: The man, fox, chicken, and sack of corn are starting on the same side of the river.'.format(0))
    for i in range(len(path)-1):
        if path[i] == '0000' and path[i+1] == '1010':
            print('{}: The man crosses the river with the chicken and leaves it on the other side.'.format(i+1))
        elif path[i] == '0001' and path[i+1] == '1011':
            print('{}: The man crosses the river with the chicken and leaves it on the other side where the sack of corn is.'.format(i+1))
        elif path[i] == '0001' and path[i+1] == '1101':
            print('{}: The man crosses the river with the fox and leaves it on the other side where the sack of corn is.'.format(i+1))
        elif path[i] == '0010' and path[i+1] == '1010':
            print('{}: The man crosses the river alone.'.format(i+1))
        elif path[i] == '0010' and path[i+1] == '1011':
            print('{}: The man crosses the river with the sack of corn and leaves it on the other side where the chicken is.'.format(i+1))
        elif path[i] == '0010' and path[i+1] == '1110':
            print('{}: The man crosses the river with the fox and leaves it on the other side where the chicken is.'.format(i+1))
        elif path[i] == '0100' and path[i+1] == '1101':
            print('{}: The man crosses the river with the sack of corn and leaves it on the other side where the fox is.'.format(i+1))
        elif path[i] == '0100' and path[i+1] == '1110':
            print('{}: The man crosses the river with the chicken and leaves it on the other side where the fox is.'.format(i+1))
        elif path[i] == '0101' and path[i+1] == '1101':
            print('{}: The man crosses the river alone.'.format(i+1))
        elif path[i] == '0101' and path[i+1] == '1111':
            print('{}: The man crosses the river with the chicken and leaves it on the other side where the fox and sack of corn are.\n'.format(i+1))
        elif path[i] == '1010' and path[i+1] == '0000':
            print('{}: The man goes back across the river with the chicken and leaves it on the starting side where the fox and sack of corn are.'.format(i+1))
        elif path[i] == '1010' and path[i+1] == '0010':
            print('{}: The man goes back across the river alone.'.format(i+1))
        elif path[i] == '1011' and path[i+1] == '0001':
            print('{}: The man goes back across the river with the chicken and leaves it on the starting side where the fox is.'.format(i+1))
        elif path[i] == '1011' and path[i+1] == '0010':
            print('{}: The man goes back across the river with the sack of corn and leaves the it on the starting side where the fox is.'.format(i+1))
        elif path[i] == '1101' and path[i+1] == '0001':
            print('{}: The man goes back across the river with the fox and leaves it on the starting side where the chicken is.'.format(i+1))
        elif path[i] == '1101' and path[i+1] == '0100':
            print('{}: The man goes back across the river with the sack of corn and leaves it on the starting side where the chicken is.'.format(i+1))
        elif path[i] == '1101' and path[i+1] == '0101':
            print('{}: The man goes back across the river alone.'.format(i+1))
        elif path[i] == '1110' and path[i+1] == '0010':
            print('{}: The man goes back across the river with the fox and leaves it on the starting side where the sack of corn is.'.format(i+1))
        elif path[i] == '1110' and path[i+1] == '0100':
            print('{}: The man goes back across the river with the sack of corn and leaves the it on the starting side where the chicken is.'.format(i+1))
    print('The man, fox, chicken, and sack of corn are now all safely across the river')

# Helper function to test the code.
# Returns the number of edges.
def count_edges(G):
    edges = 0
    for i in G.al:
        edges += len(i)
    if not G.directed:
        edges=  edges//2    
    return edges    


# Testing. 
print('-- Problem 1.1:')
# Create a graph from the distance matrix.
G, cities = al_representation('distances.txt','cities.txt')
G.display()
G.draw('Graph from Distance Matrix')
print()

# Check if the graph was made correctly.
file = open('distances.txt','r')
line = file.readline().rstrip('\n').split(',')
for i in G.al:
    for j in i:
        k = j.dest
        if int(line[k]) != -1 and j.weight != int(line[k]):
            print('Graph not equal to distance matrix')
    line = file.readline().rstrip('\n').split(',')
file.close()
print('Checked if graph matches data in distance matrix.\n')

print('-- Problem 1.2:')
# Compare the paths to those computed by hand.  
shortest_paths(G, cities)

print('-- Problem 1.3:')
# Create an MST.
mst = kruskal(G)
mst.display()
mst.draw('Minimum Spanning Tree Graph')
print()

# Check if the number of edges is 1 less than the vertices.
if count_edges(mst) != len(mst.al)-1:
    print('MST not computed correctly.')
print('Checked that the number of edges is 1 less than the number of vertices.')

# Check that the graph is connected.
# There should only be one root.
prev, dist = dijkstra(mst,0)
for i in range(len(prev)):
    path = get_path(prev,i,cities)
    if(len(path) < 2) and path != ['El Paso']:
        print('Path does not exist from {} to {}: {}\n'.format(cities[0],cities[i],path))
print('Checked there is a path from every city to every other city.\n')

print('-- Problem 1.4:')
# Compare the paths to those computed by hand.
diff_distance(G, mst, cities)

print('-- Problem 2:')
# Compare the series of steps to the actual answer of the riddle.
rowboat_problem(experiment=True)
        

    
    
    
    
    
    
    
    
    
    
