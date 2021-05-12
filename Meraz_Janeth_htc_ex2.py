import matplotlib.pyplot as plt
import numpy as np
import hash_table_chain as htc

# def same_hash_as_k(h,k):
#     sh = []
#     for b in h.bucket:
#         for i in b:
#             if h.h(k) == h.h(i.key):
#                 sh.append(i.key)
#     return sh

def same_hash_as_k(h,k):
    sh = []
    for b in h.bucket[h.h(k)]:
        sh.append(b.key)
    return sh

def invert_hash(h):
    hi = htc.HashTableChain(len(h.bucket))
    for b in h.bucket:
        for i in b:
            hi.insert(i.data,i.key)
    return hi
        
def intersection(L1,L2):
    ints = []
    h = htc.HashTableChain(len(L1) + len(L2))
    for i in L1:
        h.insert(i,[])
    for i in L2:
        if h.insert(i,[]) == -1:
            ints.append(i)
    return ints   

def difference(L1,L2):
    diff = []
    h = htc.HashTableChain(len(L1) + len(L2))
    for i in L2:
        h.insert(i,[])
    for i in L1:
        if h.insert(i,[]) == 1:
            diff.append(i)
    return diff
    
def reversed_pairs(L):
    pairs = []
    h = htc.HashTableChain(len(L))
    for i in L:
        h.insert(i,[])
        if h.retrieve(i[::-1]) != None:
            pairs.append(i)
            if i != i[::-1]:
                pairs.append(i[::-1])
    return sorted(pairs)
    
if __name__ == "__main__":  
    plt.close('all') 
    
    countries = ['Russia','Canada', 'USA', 'Brazil', 'Australia', 'China','Spain','France']
    capitals = ['Moscow','Ottawa', 'Washington', 'Brasilia', 'Canberra', 'Beijing','Madrid','Paris']
    h = htc.HashTableChain(len(countries))

    for i in range(len(countries)):
        h.insert(countries[i],capitals[i])
    h.print_table()
    '''
    Table contents:
    bucket 0: [ [Australia, Canberra] ]
    bucket 1: [ [Spain, Madrid] ]
    bucket 2: [ ]
    bucket 3: [ [Russia, Moscow] [USA, Washington] [France, Paris] ]
    bucket 4: [ [Brazil, Brasilia] ]
    bucket 5: [ ]
    bucket 6: [ [Canada, Ottawa] ]
    bucket 7: [ [China, Beijing] ]
    '''    
    
    print(same_hash_as_k(h,'Russia')) # ['Russia', 'USA', 'France']
    print(same_hash_as_k(h,'Canada')) # ['Canada']
    
    h2 = invert_hash(h)
    h2.print_table()
    '''
    Table contents:
    bucket 0: [ [Washington, USA] ]
    bucket 1: [ ]
    bucket 2: [ [Moscow, Russia] ]
    bucket 3: [ [Paris, France] ]
    bucket 4: [ [Ottawa, Canada] ]
    bucket 5: [ [Madrid, Spain] [Brasilia, Brazil] ]
    bucket 6: [ [Canberra, Australia] [Beijing, China] ]
    bucket 7: [ ]
    '''
    
    L1 = [2,3,5,7,11,13]
    L2 = [3,4,5,11,17]
        
    print(intersection(L1,L2))  # [3, 5, 11]

    print(difference(L1,L2)) # [2, 7, 13]
    
    L0=['the','rats','were','looking','at','a','star']
    L1 = ['a','lone','wolf','went','with','the','flow']
    L2 = ['anna','would','rather','write','a','while','loop','than','swim','in','the','pool']
    print(reversed_pairs(L0)) # ['a', 'rats', 'star']
    print(reversed_pairs(L1)) # ['a', 'flow', 'wolf']
    print(reversed_pairs(L2)) # ['a', 'anna', 'loop', 'pool']
    
    