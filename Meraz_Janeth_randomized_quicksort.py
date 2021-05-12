import numpy as np
import matplotlib.pyplot as plt
import time
import random

def quicksort(x):
      if len(x) < 2:
          return x
      else:
          pivot = x[0]
          less = [i for i in x[1:] if i <= pivot]
          greater = [i for i in x[1:] if i > pivot]
          return quicksort(less) + [pivot] + quicksort(greater)

def quicksort_random(x):
      if len(x) < 2:
          return x
      else:
          # Add randomization code here - use np.random.randint
          k = np.random.randint(0,len(x)-1)
          pivot = x[k]
          less = [i for i in x[:k] if i <= pivot] + [i for i in x[k+1:] if i <= pivot]
          greater = [i for i in x[:k] if i > pivot] + [i for i in x[k+1:] if i > pivot]
          return quicksort_random(less) + [pivot] + quicksort_random(greater)

if __name__ == "__main__": 
    print('====== Unsorted inputs ======')
    n = 2000       
    print('n=',n)     
    L = list(np.random.randint(1000000, size=n))
    start = time.time()
    Ls = quicksort(L)
    elapsed_time = time.time() - start
    print('Unsorted input, running time quicksort: {:7.5f} seconds'.format(elapsed_time))
    print('List comparison:',Ls==sorted(L))
    
    L = list(np.random.randint(1000000, size=n))
    start = time.time()
    Ls = quicksort_random(L)
    elapsed_time = time.time() - start
    print('Unsorted input, running time randomized quicksort: {:7.5f} seconds'.format(elapsed_time))
    print('List comparison:',Ls==sorted(L))
    
    n = 100000  
    print('n=',n)      
    L = list(np.random.randint(1000000, size=n))
    start = time.time()
    Ls = quicksort(L)
    elapsed_time = time.time() - start
    print('Unsorted input, running time: {:7.5f} seconds'.format(elapsed_time))
    print('List comparison:',Ls==sorted(L))
    
    L = list(np.random.randint(1000000, size=n))
    start = time.time()
    Ls = quicksort_random(L)
    elapsed_time = time.time() - start
    print('Unsorted input, running time randomized quicksort: {:7.5f} seconds'.format(elapsed_time))
    print('List comparison:',Ls==sorted(L))
    
    print('====== Sorted inputs ======')
    n = 2000       
    print('n=',n)     
    L = sorted(list(np.random.randint(1000000, size=n)))
    start = time.time()
    Ls = quicksort(L)
    elapsed_time = time.time() - start
    print('Unsorted input, running time quicksort: {:7.5f} seconds'.format(elapsed_time))
    print('List comparison:',Ls==sorted(L))
    
    L = sorted(list(np.random.randint(1000000, size=n)))
    start = time.time()
    Ls = quicksort_random(L)
    elapsed_time = time.time() - start
    print('Unsorted input, running time randomized quicksort: {:7.5f} seconds'.format(elapsed_time))
    print('List comparison:',Ls==sorted(L))
    
    n = 100000  
    print('n=',n)  
    
    '''
    # RecursionError: maximum recursion depth exceeded in comparison
    L = sorted(list(np.random.randint(1000000, size=n)))
    start = time.time()
    Ls = quicksort(L)
    elapsed_time = time.time() - start
    print('Unsorted input, running time quicksort: {:7.5f} seconds'.format(elapsed_time))
    print('List comparison:',Ls==sorted(L))
    '''
    
    L = sorted(list(np.random.randint(1000000, size=n)))
    start = time.time()
    Ls = quicksort_random(L)
    elapsed_time = time.time() - start
    print('Unsorted input, running time randomized quicksort: {:7.5f} seconds'.format(elapsed_time))
    print('List comparison:',Ls==sorted(L))


'''
====== Unsorted inputs ======
n= 2000
Unsorted input, running time quicksort: 0.00401 seconds
List comparison: True
Unsorted input, running time randomized quicksort: 0.01297 seconds
List comparison: True
n= 100000
Unsorted input, running time: 0.25133 seconds
List comparison: True
Unsorted input, running time randomized quicksort: 0.67422 seconds
List comparison: True
====== Sorted inputs ======
n= 2000
Unsorted input, running time quicksort: 0.17407 seconds
List comparison: True
Unsorted input, running time randomized quicksort: 0.01197 seconds
List comparison: True
n= 100000
Unsorted input, running time randomized quicksort: 0.84293 seconds
List comparison: True

'''
