"""
Course: CS 2302 
Date of last modification: July 22, 2020
Purpose: Implement a hash table and binary search tree 
    in order to retrieve all the anagrams of a large set of English words. 
    In addition, discuss the statistics and performance of each method.   
"""

import random
import time
import matplotlib.pyplot as plt
import hash_table_chain as htc
import bst

# Function opens and reads the file sent as a parameter.
# The file is traversed and each word is added to a list. 
# Each line in the file is read individually and the end of line charater is removed. 
# The file is closed and the list is returned. 
def store_words(file_name):
    file = open(file_name,'r')
    line = file.readline().rstrip('\n')
    words = []
    while line:
        if len(line) > 2:
            words += [line]
        line = file.readline().rstrip('\n')
    file.close()
    return words

# Function creates a hash table from a list.
# The list is traversed and a key is created for each word.
# The current word is added to the data of the record with the same key.
# If the key is not in the hash table, a new record is created with the key and word.
# This process continues until the whole list has been traversed. 
def create_hash(L):
    H = htc.HashTableChain(len(L))
    for w in L:
       k = ''.join(sorted(w)) 
       data = H.retrieve(k)
       if data == None:
           H.insert(k,[w])
       else:
           H.update(k,data+[w])
    return H 
  
# Function creates a binary search tree from a list.
# The list is traversed and a key is created for each word.
# The current word is added to the data of the node with the same key.
# If the key is not in any nodes in the tree, a new node is created with the key and word.
# This process continues until the whole list has been traversed. 
def create_bst(L):
    t = bst.BST() 
    L = random.sample(L,len(L))
    for w in L:
        k = ''.join(sorted(w)) 
        node = t.find(k)
        if node == None:
            t.insert(k,[w])
        else:
            node.data += [w]
    return t 

# Function displays the statistics of a bst or a hash table. 
# The type is first checked whether it is a bst or a hash table.
# If the type is bst, then a helper method is called to compute the height.
# The size and height of the bst are then returned. 
# If the type is hash table, then the load factor, longest bucket, percent of empty buckets, and percent of collisions are calculated and returned.
def statistics(data_structure):
    if type(data_structure) == bst.BST:
        height = height_bst(data_structure.root)
        return data_structure.size,height 
    if type(data_structure) == htc.HashTableChain:
        count = 0
        longest_b = 0
        empty_b = 0
        collisions = 0
        for b in data_structure.bucket:
            count+= len(b)
            if len(b) > longest_b:
                longest_b = len(b)
            if len(b) == 0:
                empty_b += 1
            if len(b) > 1:
                collisions += 1
            
        load_f = count/len(data_structure.bucket)
        # Compute the percentage.
        percent_empty = 100*empty_b/len(data_structure.bucket)
        percent_collisions =  100*collisions/len(data_structure.bucket)       
        return load_f,longest_b,percent_empty,percent_collisions

# Helper function to calculate the height of a bst.
# The longest height of a node is returned.
def height_bst(t):
    if t == None:
        return -1
    left = 1 + height_bst(t.left)
    right = 1 + height_bst(t.right)
    return max(left, right)      

# Function retrieves the anagrams for a bst or a hash table. 
# A sorted string of the word is first computed.
# If the type is bst, then the data with the sorted string as the key is returned.
# If the type is hash table, then the bucket with the sorted string as a key is traversed.
# The data of the hash table record with the sorted string as the key is returned.         
def retrieve(data_structure,w):
    k = ''.join(sorted(w)) 
    if type(data_structure) == bst.BST:
        return data_structure.find(k).data 
    if type(data_structure) == htc.HashTableChain:
        for i in data_structure.bucket[data_structure.h(k)]:
            if i.key == k:
                return i.data

L = store_words('words_alpha.txt')

# The following tests use a hash table.
# This test displaying how long it took to build a hash table.
print('Time taken to build a Hash Table:')
reps = 5
times = []
for r in range(reps):
    start = time.time()
    H = create_hash(L)
    elapsed_time = time.time() - start
    times.append(elapsed_time)
average = sum(times)/len(times)   
print('Average time taken with {} repetitions: {:7.5f} seconds'.format(reps,average))
print()

# This test displays a plot and creates a file of the time it took to retrieve each word's anagrams.
print('Time taken to Retrieve Anagrams from a Hash Table:')
reps = 3
times= []
for i in range(len(L)):
    sum_time = 0
    for r in range(reps):
        start = time.time()
        retrieve(H,L[i])
        elapsed_time = time.time() - start
        sum_time += elapsed_time
    times.append(sum_time/reps) 
    
fig, ax = plt.subplots()
plt.plot([i for i in range(len(L))],times)
ax.set_xlabel('Word Index')
ax.set_ylabel('running time (seconds)')
fig.suptitle('Running time to Retrieve Anagrams from a Hash Table', fontsize=16)
print('Plot of time taken to retrieve each word\'s anagrams created.')

# Create a file to write the time taken to retrieve the anagrams for each word.    
f = open('Meraz_Janeth_RetrievalHashTable.txt', 'w+')
f.write('Word \t\t\t\t Time taken to Retrieve Anagrams from Hash Table\n\n')
for i in range(len(L)):
    if len(L[i]) > 22:
        tab = '\t'
    elif len(L[i]) > 14:
        tab = '\t\t' 
    elif len(L[i]) > 6:
        tab = '\t\t\t'
    else:
        tab = '\t\t\t\t'
    f.write('{} {} {}\n'.format(L[i],tab,times[i]))
f.close()
print('File of time taken to retrieve each word\'s anagrams created.')
print()

# Display the statistics of the hash table. 
print('Hash Table Statistics: ')
load_f,longest_b,percent_empty,collisions = statistics(H)
print('Load Factor: {:5.2f}'.format(load_f))
print('Longest Bucket: ', longest_b)
print('Percentage of Empty Buckets: {:5.2f}%'.format(percent_empty))
print('Percent of Collisions: {:5.2f}%'.format(collisions))
print()

# The following tests use a binary search tree.
# This test displaying how long it took to build a binary search tree.
print('Time taken to build a Binary Search Tree:')
reps = 5
times = []
for r in range(reps):
    start = time.time()
    t = create_bst(L)
    elapsed_time = time.time() - start
    times.append(elapsed_time)
average = sum(times)/len(times)   
print('Average time taken with {} repetitions: {:7.5f} seconds'.format(reps,average))
print()

# This test displays a plot and creates a file of the time it took to retrieve each word's anagrams.
print('Time taken to Retrieve Anagrams from a Binary Search Tree:')
reps = 3
times = []
for i in range(len(L)):
    sum_time = 0
    for r in range(reps):
        start = time.time()
        retrieve(t,L[i])
        elapsed_time = time.time() - start
        sum_time += elapsed_time
    times.append(sum_time/reps) 
    
fig, ax = plt.subplots()
plt.plot([i for i in range(len(L))],times)
ax.set_xlabel('Word Index')
ax.set_ylabel('running time (seconds)')
fig.suptitle('Running time to Retrieve Anagrams from a BST', fontsize=16)
print('Plot of time taken to retrieve each word\'s anagrams created.')

# Create a file to write the time taken to retrieve the anagrams for each word.     
f = open('Meraz_Janeth_RetrievalBST.txt', 'w+')
f.write('Word \t\t\t\t Time taken to Retrieve Anagrams from BST\n\n')
for i in range(len(L)):
    if len(L[i]) > 22:
        tab = '\t'
    elif len(L[i]) > 14:
        tab = '\t\t' 
    elif len(L[i]) > 6:
        tab = '\t\t\t'
    else:
        tab = '\t\t\t\t'
    f.write('{} {} {}\n'.format(L[i],tab,times[i]))
f.close()
print('File of time taken to retrieve each word\'s anagrams created.')
print()

# Display the statistics of the binary search tree. 
print('Binary Search Tree Statistics: ')
num_nodes, height = statistics(t)
print('Number of Nodes: ', num_nodes)
print('Height of tree:', height)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
