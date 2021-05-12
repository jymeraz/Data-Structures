import numpy as np
from math import *
import time

def subsetsum_v0(S,goal): 
    # Determines if there is a subset of S that adds up to g, where elements of S are positive integers
    # Returns the subset that adds up to g if it exists or None if no such subset exists
    if goal==0:
        return []
    if len(S)==0:
        return None # There is no solution
    subset = subsetsum_v0(S[1:],goal-S[0]) # Take S[0]
    if subset != None: # There is a solution when taking S[0]
        return [S[0]] + subset
    else:   # There is no solution when taking S[0], try leaving S[0]
        return subsetsum_v0(S[1:],goal) # Don't take S[0]

def subsetsum_v1(S,goal): 
    # Determines if there is a subset of S that adds up to g, where elements of S are positive integers
    # Returns the subset that adds up to g if it exists or None if no such subset exists
    if goal==0:
        return []
    if goal<0 or len(S)==0:
        return None # There is no solution
    subset = subsetsum_v1(S[1:],goal-S[0]) # Take S[0]
    if subset != None: # There is a solution when taking S[0]
        return [S[0]] + subset
    else:   # There is no solution when taking S[0], try leaving S[0]
        return subsetsum_v1(S[1:],goal) # Don't take S[0]
    
def subsetsum_v2(S,goal,remain): 
    # Determines if there is a subset of S that adds up to g, where elements of S are positive integers
    # Returns the subset that adds up to g if it exists or None if no such subset exists
    if goal==0:
        return []
    if goal>remain or goal<0 or len(S)==0:
        return None # There is no solution
    subset = subsetsum_v2(S[1:],goal-S[0],remain-S[0]) # Take S[0]
    if subset != None: # There is a solution when taking S[0]
        return [S[0]] + subset
    else:   # There is no solution when taking S[0], try leaving S[0]
        return subsetsum_v2(S[1:],goal,remain-S[0]) # Don't take S[0]
     
def partition(S):
    S.sort(reverse=True)
    S1 = subsetsum_v2(S,sum(S)//2,sum(S))
    if S1 == None or sum(S)%2 != 0:
        return None
    return [S1] + [[i for i in S if i not in S1]]

if __name__ == "__main__":  
    
    show_results = False  # Set to True if you want to see subsets found for every goal
    
    mySet =[12, 997, 5, 53, 452, 2, 25, 2001, 107, 221]
    
    print('Original version')
    solutions = []
    start = time.time()           
    for goal in range(sum(mySet)+5):
        solutions.append(subsetsum_v0(mySet,goal))
    elapsed_time = time.time() - start 
    print('Running time: {:7.5f} seconds'.format(elapsed_time))
    no_solution = len([x for x in solutions if x ==None])
    print('Evaluated {} instances, {} had a solution, {} had no solution'.format(len(solutions), len(solutions) - no_solution, no_solution))
    
    print('\nStopping backtracking if goal is negative')
    solutions = []
    start = time.time()           
    for goal in range(sum(mySet)+5):
        solutions.append(subsetsum_v1(mySet,goal))
    elapsed_time = time.time() - start 
    print('Running time: {:7.5f} seconds'.format(elapsed_time))
    no_solution = len([x for x in solutions if x ==None])
    print('Evaluated {} instances, {} had a solution, {} had no solution'.format(len(solutions), len(solutions) - no_solution, no_solution))
    
    print('\nUsing sorted inputs to find unfeasible solutions earlier in the search')
    mySet.sort(reverse=True)
    solutions = [] 
    start = time.time()         
    for goal in range(sum(mySet)+5):
        solutions.append(subsetsum_v1(mySet,goal))
    elapsed_time = time.time() - start 
    print('Running time: {:7.5f} seconds'.format(elapsed_time))
    no_solution = len([x for x in solutions if x ==None])
    print('Evaluated {} instances, {} had a solution, {} had no solution'.format(len(solutions), len(solutions) - no_solution, no_solution))
    
    print('\nStopping backtracking if sum of remaining items is less than goal')
    mySet.sort(reverse=True)
    solutions = []
    start = time.time()           
    for goal in range(sum(mySet)+5):
        solutions.append(subsetsum_v2(mySet,goal,sum(mySet)))
    elapsed_time = time.time() - start 
    print('Running time: {:7.5f} seconds'.format(elapsed_time))
    no_solution = len([x for x in solutions if x ==None])
    print('Evaluated {} instances, {} had a solution, {} had no solution'.format(len(solutions), len(solutions) - no_solution, no_solution))
    
    print('\nPartition')
    mySet.sort(reverse=True)
    print(mySet,'->',partition(mySet))
    s = [2,5,7,11,14]
    print(s,'->',partition(s))
    s = [2,5,7,11,15]
    print(s,'->',partition(s))
    s = mySet + [127]
    print(s,'->',partition(s))
    # s = [100]
    # print(s,'->',partition(s))
    
    if show_results:
        for goal,solution in enumerate(solutions):
            print('Goal:',goal,'  Solution:',subsetsum(mySet,goal))
'''
Program results:
         
Original version
Running time: 1.61668 seconds
Evaluated 3880 instances, 1024 had a solution, 2856 had no solution

Stopping backtracking if goal is negative
Running time: 1.05621 seconds
Evaluated 3880 instances, 1024 had a solution, 2856 had no solution

Using sorted inputs to find unfeasible solutions earlier in the search
Running time: 0.74502 seconds
Evaluated 3880 instances, 1024 had a solution, 2856 had no solution

Stopping backtracking if sum of remaining items is less than goal
Running time: 0.01991 seconds
Evaluated 3880 instances, 1024 had a solution, 2856 had no solution  

Partition
[2001, 997, 452, 221, 107, 53, 25, 12, 5, 2] -> None
[2, 5, 7, 11, 14] -> None
[2, 5, 7, 11, 15] -> [[2, 7, 11], [5, 15]]
[2001, 997, 452, 221, 107, 53, 25, 12, 5, 2, 127] -> [[2001], [997, 452, 221, 107, 53, 25, 12, 5, 2, 127]]
          
'''       