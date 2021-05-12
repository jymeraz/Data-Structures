import matplotlib.pyplot as plt
import numpy as np
import btree

def print_data(T):
    if type(T)==btree.BTree:
        T=T.root
    if T.is_leaf:
        for d in T.data:
            print(d,end=' ')
    else:
        print_data(T.child[0])
        for i in range(len(T.data)):
            print(T.data[i],end=' ')
            print_data(T.child[i+1])

def smallest(T):
    if type(T) == btree.BTree:
        T = T.root
    if T.is_leaf:
        return T.data[0]
    return smallest(T.child[0])

def largest(T):
    if type(T) == btree.BTree:
        T = T.root
    if T.is_leaf:
        return T.data[-1]
    return largest(T.child[-1])

def numNodes(T):
    count = 1
    if type(T)==btree.BTree:
        T=T.root
    if T.is_leaf:
        return 1
    else:
        for i in range(len(T.child)):
            count += numNodes(T.child[i])
    return count

def numItems(T):
    if type(T)==btree.BTree:
        T=T.root
    count = len(T.data)
    if T.is_leaf:
        return len(T.data)
    else:
        for i in range(len(T.child)):
            count += numItems(T.child[i])
    return count


if __name__ == "__main__":
    plt.close('all')
    T = btree.BTree()

    nums = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
  
    for num in nums:
        T.insert(num)
    T.draw()

    print_data(T)
    print()

    print(smallest(T))  
    print(largest(T))   
    print(numNodes(T))  
    print(numItems(T))  
    
    t = T.root
    print(t.data)
    print(t.child[1])


'''
Program output:
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 
1
30
9
30
'''