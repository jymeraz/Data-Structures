"""
Course: CS 2302 
Author: Janeth Meraz
Assignment: Lab 3
Instructor: Olac Fuentes
T.A.: Oscar Galindo
I.A.: Seth Flores
Date of last modification: 07/08/2020 
Purpose: Implement bst sort and btree sort algorithms to sort Lists and evaluate 
    their respective running times against other sorting algorithms. 
    The different inputs include sorted and unsorted Lists of differing sizes.     
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import singly_linked_list as sll
import bst
import btree 

# Function inserts the elements of a List to a binary search tree.
# The tree is traversed using a helper method that returns a sorted List.
# The pointers of head and tail are made sure to be pointing to the correct elements. 
def bst_sort(L):
    tree = bst.BST()
    t = L.head
    while t != None:
        tree.insert(t.data)
        t = t.next
    L.head = bst_list(tree.root).head
    t = L.head
    while t.next != None:
        t = t.next
    L.tail = t

# Recursive function returns a sorted list through traversing a binary search tree.
# The left nodes of the tree are added to the list first.
# Then, the middle node is added, followed by the nodes in the right. 
# The complete List is returned at the end. 
def bst_list(r):
    L = sll.List()
    if r == None:
        return
    
    left = bst_list(r.left)
    # If the left traversal was not empty, add the elements of the returned List to the current List.
    # Ensure the tail points to the correct node. 
    if left != None:
        L.append(left.head.data)
        L.tail.next = left.head.next
        L.tail = left.tail
     
    # Add the middle node to the List.
    # If there is no head, add a head. Otherwise, add the node to the end of the List.
    # Ensure the tail points to the correct node.
    if L.head == None:
        L.append(r.data)
    else: 
          l = L.head
          while l.next != None:
              l = l.next
          L.tail = l
          new_node = sll.ListNode(r.data)
          L.tail.next = new_node
          L.tail = L.tail.next
         
    right = bst_list(r.right)
    # If the right traversal was not empty, add the elements of the returned List to the current List.
    # Ensure the tail points to the correct node. 
    if right != None:
        L.append(right.head.data)
        L.tail.next = right.head.next
        L.tail = right.tail
    return L

# Function inserts the elements of a List to a btree.
# The tree is traversed using a helper method that returns a sorted List.
# The pointers of head and tail are made sure to be pointing to the correct elements. 
def btree_sort(L):
    tree = btree.BTree()
    t = L.head
    while t != None:
        tree.insert(t.data)
        t = t.next
    L.head = btree_list(tree.root).head
    t = L.head
    while t.next != None:
        t = t.next
    L.tail = t

# Recursive function returns a sorted list through traversing a btree.
# The first child nodes of the btree are added to the List first.
# Then, the data in the midde is added, followed by the child nodes on the right of the midde data. 
# The complete List is returned at the end. 
def btree_list(t):
    L = sll.List()
    if t.is_leaf:
        for d in t.data:
            L.append(d)
        return L
    else:
        # Add the elements of the first child to the List.
        # Update the head and tail pointers.
        new_list = btree_list(t.child[0])
        L.append(new_list.head.data)
        L.head.next = new_list.head.next
        L.tail = new_list.tail
        temp = L.tail
        
        # Add the first data value to the List.
        # Add the child node immediadely to the right of this data value.
        # Continue until all data values and chid nodes have been added to the List. 
        # Update the head and tail pointers.
        for i in range(len(t.data)):
            new_node = sll.ListNode(t.data[i])
            temp.next = new_node
            temp = temp.next
            
            new_list = btree_list(t.child[i+1])
            temp.next = new_list.head
            L.tail = new_list.tail
            temp = L.tail
    return L

# Function sorts the List through selection sort
# The minimum value is found and the data is swapped with the data in the head.
# The next minimum value excluding the head is found and swapped with the data in the node after the head.
# Process is repeated until the whole List is sorted.
def selection_sort(L):
    t = L.head
    while t != None:
        minimum = t
        iterator = t
        while iterator != None:
            # Keep track of the node with the minimum value. 
            if iterator.data < minimum.data:
                minimum = iterator
            iterator = iterator.next
        t.data, minimum.data = minimum.data, t.data
        # Begin in the next node. 
        t = t.next

# Function sorts the List through bubble sort
# Starting from the beginning, if the next node's data is smaller than the current node's, swap their data.
# Once the end is reached, start at the beginning again.
# Repeat this process until no data is swapped.
def bubble_sort(L):
    t = L.head
    # Initialize a boolean variable to check if data is swapped. 
    swapped = True
    while swapped:
        swapped = False
        while t.next != None:
            if t.data > t.next.data:
                t.data, t.next.data = t.next.data, t.data
                swapped = True
            t = t.next
        t = L.head

# Wrapper function sorts the List through merge sort.
# Set the head of the List to the node the wrapper function sorting the List returns.
# Set the tail to point to the last node in the list. 
def merge_sort(L):
    L.head = merge_sort_n(L.head) 
    t = L.head
    while t.next != None:
       t = t.next
    L.tail = t

# Recursive function that separates the list in half and returns the two sorted halves merged. 
# The middle node is found through a helper method.
# The List is separated from the beginning to the middle and from the node after the middle to the end.
# The two halves are sent back to the function through recursive calls where the process is repeated until there are single nodes.
# Once there are single nodes, the nodes begin to be merged in order until the full List is merged.
def merge_sort_n(t):
    if t == None or t.next == None:
        return t

    mid = middle(t)
    after_mid = mid.next
    mid.next = None
    
    left = merge_sort_n(t)
    right = merge_sort_n(after_mid)
    
    # Return the first node in the merged halves. 
    return merged_halves(left, right) 

# Function returns the first node in the merged List of the two halves. 
# Function takes two Lists as parameters.
# If either List is empty, return the other List.
# Compare the data in the two List and save the node with the smallest data as the first node in the merged List. 
# Iterate through the two Lists while the node with the smallest data in each loop.
# Once a List is empty, set the next value of the merged List to the List that is not empty.
# Once the halves have been merged, return the first node of the List.
def merged_halves(t1,t2):    
    if t1 == None:
        return t2
    if t2 == None:
        return t1
    
    # Save the reference to the first node.
    if t1.data < t2.data:
        t = t1
        t1 = t1.next
    else:
        t = t2
        t2 = t2.next
    temp = t
    
    # Iterate through each List while saving the reference to the smallest node in the merged List.
    while t1 != None and t2 != None:
        if t1.data < t2.data:
            temp.next = t1
            t1 = t1.next
        else:
            temp.next = t2
            t2 = t2.next
        temp = temp.next  
    
    if t1 == None:
        temp.next = t2
    if t2 == None:
        temp.next = t1
    return t

# Function returns the node in the middle of the List. 
# Set two iterators that traverse the List in different speeds.
# The first iterator advances each time, and the second iterator advances every other time. 
# Once the first iterator reaches the end, the second iterator is in the middle.
# Return the second iterator.          
def middle(t):
    fast_iter,mid,advance = t,t,False
    while fast_iter.next != None and fast_iter.next.next != None:
        fast_iter = fast_iter.next
        if advance:
            mid = mid.next
        # Negate the boolean variable.
        # This causes the second iterator to advance every other loop. 
        advance = ~ advance
    return mid

# Wrapper function sorts the List through quick sort.
# Set the head of the List to the node the wrapper function sorting the List returns.
# Set the tail to point to the last node in the list.
def quick_sort(L):
    L.head = quick_sort_n(L.head)
    t = L.head
    while t.next!= None:
        t = t.next
    L.tail = t

# Recursive function partitionns the List in two and calls the function again with each partition. 
# The node at the partition is found through a helper function.
# The List is separated in two Lists.
# One List is the beginning of the current List to the partitio node.
# The second List is the node after the partition node to the end.
# Once nodes of size one are reached, the partitions are combined where the right partition comes right after the left.
# The first node of the combined partitioned is returned. 
def quick_sort_n(t):
    if t == None or t.next == None:
        return t
    
    partition_node = partition(t)
    after_partition = partition_node.next
    partition_node.next = None
    
    left = quick_sort_n(t)
    right = quick_sort_n(after_partition)
    
    temp = left
    while temp.next!= None:
        temp = temp.next
    temp.next = right

    return t

# Function returns the node separating two partitions of one List.
# The pivot is chosen as the first node in the List.
# The List is traversed and if a node has data less than the pivot, then it is inserted before the first node.
# After the whole List is traversed, the pivot node is returned.
def partition(t):
    if t == None or t.next == None:
        return t
    
    pivot = t
    temp = t.next
    previous = t
    while temp != None:
        if temp.data < pivot.data:
            previous.next = previous.next.next
            temp.next = t
            temp = previous.next
        else: 
            previous = temp
            temp = temp.next
    return pivot

# Function returns the length of the List.
def length(L):
    t = L.head
    c = 0
    while t!=None:
        c+=1
        t=t.next
    return c

# Function checks if the List is sorted.
# Return False if the node next to the current node has smaller data
# Return True once the whole List is iterated through.
def is_sorted(L):
    t = L.head
    if t == None:
        return True
    while t.next!=None:
        if t.data > t.next.data:
            return False
        t=t.next
    return True
 
    
# Test for bst Sort with an unsorted Linked List
print('Test for bst sort with an unsorted List') 
reps = 5
first_n, last_n, step_n = 10000, 200000, 10000
times, sizes = [], []
for n in range(first_n, last_n, step_n):
    sum_time = 0
    for r in range(reps):
        L1 = sll.List()
        # Create an unsorted List
        L1.extend(list(np.random.randint(1000000, size=n)))
        start = time.time()
        bst_sort(L1)
        elapsed_time = time.time() - start
        sum_time += elapsed_time
        if not is_sorted(L1):
            print("Error. List is not sorted.") # Print an error message if the List was not sorted.
        if length(L1) != n:
            print("Error. Length of List has changed.") # Print an error message if the List lost/gained nodes.
    times.append(sum_time/reps) # Display average time per repetition
    sizes.append(n)
    print('List length: {:3}, running time: {:7.5f} seconds'.format(sizes[-1],times[-1]))
    
fig, ax = plt.subplots()
plt.plot(sizes,times)
ax.set_xlabel('n')
ax.set_ylabel('running time (seconds)')
fig.suptitle('Running time for bst sorting algorithm on an unsorted List', fontsize=16)
print()

# Test for bst Sort with a sorted Linked List
print('Test for bst sort with a sorted List') 
reps = 5
first_n, last_n, step_n = 100, 3000, 100
times, sizes = [], []
for n in range(first_n, last_n, step_n):
    sum_time = 0
    for r in range(reps):
        L1 = sll.List()
        # Create a sorted List
        L1.extend(list(np.arange(n)))
        start = time.time()
        bst_sort(L1)
        elapsed_time = time.time() - start
        sum_time += elapsed_time
        if not is_sorted(L1):
            print("Error. List is not sorted.") # Print an error message if the List was not sorted.
        if length(L1) != n:
            print("Error. Length of List has changed.") # Print an error message if the List lost/gained nodes.
    times.append(sum_time/reps) # Display average time per repetition
    sizes.append(n)
    print('List length: {:3}, running time: {:7.5f} seconds'.format(sizes[-1],times[-1]))
  
fig, ax = plt.subplots()
plt.plot(sizes,times)
ax.set_xlabel('n')
ax.set_ylabel('running time (seconds)')
fig.suptitle('Running time for bst sorting algorithm on a sorted List', fontsize=16)
print() 

# Test for btree Sort with an unsorted Linked List
print('Test for btree sort with an unsorted List') 
reps = 5
first_n, last_n, step_n = 10000, 200000, 10000
times, sizes = [], []
for n in range(first_n, last_n, step_n):
    sum_time = 0
    for r in range(reps):
        L1 = sll.List()
        # Create an unsorted List
        L1.extend(list(np.random.randint(1000000, size=n)))
        start = time.time()
        btree_sort(L1)
        elapsed_time = time.time() - start
        sum_time += elapsed_time
        if not is_sorted(L1):
            print("Error. List is not sorted.") # Print an error message if the List was not sorted.
        if length(L1) != n:
            print("Error. Length of List has changed.") # Print an error message if the List lost/gained nodes.
    times.append(sum_time/reps) # Display average time per repetition
    sizes.append(n)
    print('List length: {:3}, running time: {:7.5f} seconds'.format(sizes[-1],times[-1]))
    
fig, ax = plt.subplots()
plt.plot(sizes,times)
ax.set_xlabel('n')
ax.set_ylabel('running time (seconds)')
fig.suptitle('Running time for btree sorting algorithm on an unsorted List', fontsize=16)
print()

# Test for btree Sort with a sorted Linked List
print('Test for btree sort with a sorted List') 
reps = 5
first_n, last_n, step_n = 10000, 200000, 10000
times, sizes = [], []
for n in range(first_n, last_n, step_n):
    sum_time = 0
    for r in range(reps):
        L1 = sll.List()
        # Create a sorted List
        L1.extend(list(np.arange(n)))
        start = time.time()
        btree_sort(L1)
        elapsed_time = time.time() - start
        sum_time += elapsed_time
        if not is_sorted(L1):
            print("Error. List is not sorted.") # Print an error message if the List was not sorted.
        if length(L1) != n:
            print("Error. Length of List has changed.") # Print an error message if the List lost/gained nodes.
    times.append(sum_time/reps) # Display average time per repetition
    sizes.append(n)
    print('List length: {:3}, running time: {:7.5f} seconds'.format(sizes[-1],times[-1]))
  
fig, ax = plt.subplots()
plt.plot(sizes,times)
ax.set_xlabel('n')
ax.set_ylabel('running time (seconds)')
fig.suptitle('Running time for btree sorting algorithm on a sorted List', fontsize=16)
print() 

# # Test for Selection Sort with an unsorted Linked List
# print('Test for selection sort with an unsorted List') 
# reps = 5
# first_n, last_n, step_n = 200, 5500, 200
# times, sizes = [], []
# for n in range(first_n, last_n, step_n):
#     sum_time = 0
#     for r in range(reps):
#         L1 = sll.List()
#         # Create an unsorted List
#         L1.extend(list(np.random.randint(1000000, size=n)))
#         start = time.time()
#         selection_sort(L1)
#         elapsed_time = time.time() - start
#         sum_time += elapsed_time
#         if not is_sorted(L1):
#             print("Error. List is not sorted.") # Print an error message if the List was not sorted.
#         if length(L1) != n:
#             print("Error. Length of List has changed.") # Print an error message if the List lost/gained nodes.
#     times.append(sum_time/reps) # Display average time per repetition
#     sizes.append(n)
#     print('List length: {:3}, running time: {:7.5f} seconds'.format(sizes[-1],times[-1]))
    
# fig, ax = plt.subplots()
# plt.plot(sizes,times)
# ax.set_xlabel('n')
# ax.set_ylabel('running time (seconds)')
# fig.suptitle('Running time for selection sort algorithm on an unsorted List', fontsize=16)
# print()

# # Test for Selection Sort with a sorted Linked List
# print('Test for selection sort with a sorted List') 
# reps = 5
# first_n, last_n, step_n = 200, 5500, 200
# times, sizes = [], []
# for n in range(first_n, last_n, step_n):
#     sum_time = 0
#     for r in range(reps):
#         L1 = sll.List()
#         # Create a sorted List
#         L1.extend(list(np.arange(n)))
#         start = time.time()
#         selection_sort(L1)
#         elapsed_time = time.time() - start
#         sum_time += elapsed_time
#         if not is_sorted(L1):
#             print("Error. List is not sorted.") # Print an error message if the List was not sorted.
#         if length(L1) != n:
#             print("Error. Length of List has changed.") # Print an error message if the List lost/gained nodes.
#     times.append(sum_time/reps) # Display average time per repetition
#     sizes.append(n)
#     print('List length: {:3}, running time: {:7.5f} seconds'.format(sizes[-1],times[-1]))
       
# fig, ax = plt.subplots()
# plt.plot(sizes,times)
# ax.set_xlabel('n')
# ax.set_ylabel('running time (seconds)')
# fig.suptitle('Running time for selection sort algorithm on a sorted List', fontsize=16)
# print()

# # Test for Bubble Sort with an unsorted Linked List
# print('Test for bubble sort with an unsorted List') 
# reps = 5
# first_n, last_n, step_n = 200, 5500, 200
# times, sizes = [], []
# for n in range(first_n, last_n, step_n):
#     sum_time = 0
#     for r in range(reps):
#         L1 = sll.List()
#         # Create an unsorted List
#         L1.extend(list(np.random.randint(1000000, size=n)))
#         start = time.time()
#         bubble_sort(L1)
#         elapsed_time = time.time() - start
#         sum_time += elapsed_time
#         if not is_sorted(L1):
#             print("Error. List is not sorted.") # Print an error message if the List was not sorted.
#         if length(L1) != n:
#             print("Error. Length of List has changed.") # Print an error message if the List lost/gained nodes.
#     times.append(sum_time/reps) # Display average time per repetition
#     sizes.append(n)
#     print('List length: {:3}, running time: {:7.5f} seconds'.format(sizes[-1],times[-1]))
    
# fig, ax = plt.subplots()
# plt.plot(sizes,times)
# ax.set_xlabel('n')
# ax.set_ylabel('running time (seconds)')
# fig.suptitle('Running time for bubble sort algorithm on an unsorted List', fontsize=16)
# print()

# # Test for Bubble Sort with a sorted Linked List
# print('Test for bubble sort with a sorted List') 
# reps = 5
# first_n, last_n, step_n = 200, 5500, 200
# times, sizes = [], []
# for n in range(first_n, last_n, step_n):
#     sum_time = 0
#     for r in range(reps):
#         L1 = sll.List()
#         # Create a sorted List
#         L1.extend(list(np.arange(n)))
#         start = time.time()
#         bubble_sort(L1)
#         elapsed_time = time.time() - start
#         sum_time += elapsed_time
#         if not is_sorted(L1):
#             print("Error. List is not sorted.") # Print an error message if the List was not sorted.
#         if length(L1) != n:
#             print("Error. Length of List has changed.") # Print an error message if the List lost/gained nodes.
#     times.append(sum_time/reps) # Display average time per repetition
#     sizes.append(n)
#     print('List length: {:3}, running time: {:7.5f} seconds'.format(sizes[-1],times[-1]))
    
# fig, ax = plt.subplots()
# plt.plot(sizes,times)
# ax.set_xlabel('n')
# ax.set_ylabel('running time (seconds)')
# fig.suptitle('Running time for bubble sort algorithm on a sorted List', fontsize=16)
# print()

# # Test for Merge Sort with an unsorted Linked List
# print('Test for merge sort with an unsorted List') 
# reps = 5
# first_n, last_n, step_n = 2000, 30000, 2000
# times, sizes = [], []
# for n in range(first_n, last_n, step_n):
#     sum_time = 0
#     for r in range(reps):
#         L1 = sll.List()
#         # Create an unsorted List
#         L1.extend(list(np.random.randint(1000000, size=n)))
#         start = time.time()
#         merge_sort(L1)
#         elapsed_time = time.time() - start
#         sum_time += elapsed_time
#         if not is_sorted(L1):
#             print("Error. List is not sorted.") # Print an error message if the List was not sorted.
#         if length(L1) != n:
#             print("Error. Length of List has changed.") # Print an error message if the List lost/gained nodes.
#     times.append(sum_time/reps) # Display average time per repetition
#     sizes.append(n)
#     print('List length: {:3}, running time: {:7.5f} seconds'.format(sizes[-1],times[-1]))
       
# fig, ax = plt.subplots()
# plt.plot(sizes,times)
# ax.set_xlabel('n')
# ax.set_ylabel('running time (seconds)')
# fig.suptitle('Running time for merge sort algorithm on an unsorted List', fontsize=16)
# print()

# # Test for Merge Sort with a sorted Linked List
# print('Test for merge sort with a sorted List') 
# reps = 5
# first_n, last_n, step_n = 2000, 30000, 2000
# times, sizes = [], []
# for n in range(first_n, last_n, step_n):
#     sum_time = 0
#     for r in range(reps):
#         L1 = sll.List()
#         # Create a sorted List
#         L1.extend(list(np.arange(n)))
#         start = time.time()
#         merge_sort(L1)
#         elapsed_time = time.time() - start
#         sum_time += elapsed_time
#         if not is_sorted(L1):
#             print("Error. List is not sorted.") # Print an error message if the List was not sorted.
#         if length(L1) != n:
#             print("Error. Length of List has changed.") # Print an error message if the List lost/gained nodes.
#     times.append(sum_time/reps) # Display average time per repetition
#     sizes.append(n)
#     print('List length: {:3}, running time: {:7.5f} seconds'.format(sizes[-1],times[-1]))
       
# fig, ax = plt.subplots()
# plt.plot(sizes,times)
# ax.set_xlabel('n')
# ax.set_ylabel('running time (seconds)')
# fig.suptitle('Running time for merge sort algorithm on a sorted List', fontsize=16)
# print()

# # Test for Quick Sort with an unsorted Linked List
# print('Test for quick sort with an unsorted List') 
# reps = 5
# first_n, last_n, step_n = 2000, 30000, 2000
# times, sizes = [], []
# for n in range(first_n, last_n, step_n):
#     sum_time = 0
#     for r in range(reps):
#         L1 = sll.List()
#         # Create an unsorted List
#         L1.extend(list(np.random.randint(1000000, size=n)))
#         start = time.time()
#         quick_sort(L1)
#         elapsed_time = time.time() - start
#         sum_time += elapsed_time
#         if not is_sorted(L1):
#             print("Error. List is not sorted.") # Print an error message if the List was not sorted.
#         if length(L1) != n:
#             print("Error. Length of List has changed.") # Print an error message if the List lost/gained nodes.
#     times.append(sum_time/reps) # Display average time per repetition
#     sizes.append(n)
#     print('List length: {:3}, running time: {:7.5f} seconds'.format(sizes[-1],times[-1]))

# fig, ax = plt.subplots()
# plt.plot(sizes,times)
# ax.set_xlabel('n')
# ax.set_ylabel('running time (seconds)')
# fig.suptitle('Running time for quick sort algorithm on an unsorted List', fontsize=16)
# print()

# # Test for Quick Sort with a sorted Linked List
# print('Test for quick sort with a sorted List') 
# reps = 5
# first_n, last_n, step_n = 200, 3000, 200
# times, sizes = [], []
# for n in range(first_n, last_n, step_n):
#     sum_time = 0
#     for r in range(reps):
#         L1 = sll.List()
#         # Create a sorted List
#         L1.extend(list(np.arange(n)))
#         start = time.time()
#         quick_sort(L1)
#         elapsed_time = time.time() - start
#         sum_time += elapsed_time
#         if not is_sorted(L1):
#             print("Error. List is not sorted.") # Print an error message if the List was not sorted.
#         if length(L1) != n:
#             print("Error. Length of List has changed.") # Print an error message if the List lost/gained nodes.
#     times.append(sum_time/reps) # Display average time per repetition
#     sizes.append(n)
#     print('List length: {:3}, running time: {:7.5f} seconds'.format(sizes[-1],times[-1]))
       
# fig, ax = plt.subplots()
# plt.plot(sizes,times)
# ax.set_xlabel('n')
# ax.set_ylabel('running time (seconds)')
# fig.suptitle('Running time for quick sort algorithm on a sorted List', fontsize=16)
# print()



