# Introduction to Python exercise
import numpy as np

# Exercise 1
def divisible(a,b):
    # Return True if a divided by b does not produce a remainder.
    return a%b == 0

# Exercise 2    
def prime(n):
    # Return False if n is divisible by a number less than n.
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Exercise 3
def sum_digits(n):
    # Sum the digit in the ones place, then remove it.
    # Repeat this process until all digits have been added.
    result = 0
    while n > 0:
        result += n%10
        n = n // 10
    return result

# Exercise 4
def reverse(s):
    # Concatenate the end of the given string to a new string.
    # Repeat this process until the whole string has been concatenated.
    newString = ''
    for i in range(len(s)):
        newString += s[-(i+1)]
    return newString

# Exercise 5
def remove_vowels(s):
    # Concatenate the values in a string if they are not part of the created list of vowels.
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for i in range(len(s)):
        if not s[i] in vowels:
            result += s[i]   
    return result

# Exercise 6
def pal(s):
    # Return False if the first and last elements are not equal.
    # Remove and compare the first and last elements of the string until there are zero or 1 values.
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return pal(s[1:-1])

# Exercise 7
def max_array(A):
    # Save the maximum element as the first element of the given array.
    # Iterate through the array and compare the max element to each value.
    # If a different max value is found, update max.
    max = A[0]
    for i in range(len(A)):
        if A[i] > max:
            max = A[i]
    return max

# Exercise 8
def find(A,x):
    # Iterate through the array and check if the each element is equal to the target number.
    # Once an element is equal to the target number, return the index of the element.
    # Return -1 if it was not found.
    for i in range(len(A)):
        if A[i] == x:
            return i
    return -1

# Exercise 9
def sum_array(A):
    # Iterate through the given array and sum its elements.
    sum = 0
    for i in A:
        sum += i
    return sum

# Exercise 10
def replace_array(A,x,y):
    # Iterate through the array.
    # If the element is equal to x, change the value of that element to y
    for i in range(len(A)):
        if A[i] == x:
            A[i] = y
 
# Exercise 11        
def is_square(A):
    # Check that the number of elements in each row is equal to the number of rows.
    # Return False once an inequality is found, else return True
    rows = len(A)
    for i in range(len(A)):
        if rows != len(A[i]):
            return False
    return True

# Exercise 12    
def diagonal_sum(A):
    # Add the elements with equal row and column indices. 
    sum = 0
    for i in range(len(A)):
        sum += A[i,i]
    return sum

# Exercise 13
def sec_diagonal_sum(A):
    # Add the elements starting from the first row and last column.
    # Increase the number of the row and decrease the number of the column by 1 each time.
    sum = 0
    for i in range(len(A)):
        sum += A[-len(A)+i,-(i+1)]
    return sum

# Exercise 14
def diagonal(A):
   # Create a new array and add the elements with the same indices in the given array to it.
   result = np.zeros(len(A), dtype=int)
   for i in range(len(A)):
       result[i] = A[i,i]
   return result
 
# Exercise 15
def sec_diagonal(A):
   # Create a new array.
   # Add the elements starting from the first row and last column to the new array.
   # Increase the number of the row and decrease the number of the column by 1 each time.
   result = np.zeros(len(A), dtype=int)
   for i in range(len(A)):
       result[i] = A[-len(A)+i,-(i+1)]
   return result

# Exercise 16
def swap_rows(A,i,j):
    # Create a new array with the same elements of the given array.
    # Swap the rows i and j.
    # Save A[i] in a temporary variable in order to avoid overwritting it in the new array.
    result = np.array(A,dtype=int)
    temp = A[i]
    result[i] = result[j]
    result[j] = temp
    return result

# Exercise 17
def swap_columns(A,i,j):
   # Create a new array with the same elements of the given array.
   # Iterate through the rows of the array and swap each element with colum index i with column index j. 
   result = np.array(A)
   for k in range(len(result)):
       temp = A[k,i]
       result[k,i] = result[k,j]
       result[k,j] = temp
   return result

# Exercise 18
def replace_max_array(A,x):
    # Create a new array with the same elements of the given array.
    # Find the indices of the max element and replace it with x.
    result = np.array(A,dtype=int)
    row = 0
    col = 0
    for i in range(len(result)):
        for j in range(len(result[i])):
            if result[i,j] > result[row,col]:
                row = i
                col = j
    result[row,col] = x
    return result  

# Exercise 19
def greater_than_list(L,x):
    # Iterate through the given list and check if each element is larger than the given value of x.
    # If the element is larger than x, add it to a separate list.
    G = []
    for i in range(len(L)):
        if L[i] > x:
            G.append(L[i])
    return G

# Exercise 20
def split(L):
    # Return the lists with even indices and odd indices.
    return L[::2], L[1::2] 

# Exercise 21
def merge(L1,L2):
    # Add the values in L1 and L2 to a new list in order from smallest to largest by comparing each element.
    # Once one list reaches its end, add the remaining elements of the other list to the combined list.
    # Return the merged list.
    merged = []
    firstIter = 0
    secondIter = 0
    
    while firstIter < len(L1) and secondIter < len(L2):
        if L1[firstIter] < L2[secondIter]:
            merged.append(L1[firstIter])
            firstIter += 1
        else:
            merged.append(L2[secondIter])
            secondIter += 1
    
    while firstIter < len(L1):
        merged.append(L1[firstIter])
        firstIter += 1
    while secondIter < len(L2):
        merged.append(L2[secondIter])
        secondIter += 1
    return merged

# Exercise 22
def split_pivot(L):
    # Create two separate lists for the elements smaller than the pivot and the elements greater than the pivot.
    # If the element is smaller than the pivot, add it to the first list.
    # If the element is greater than the pivot, add it to the second list.
    smaller = []
    greater = []
    for i in L:
        if i >= L[0]:
            greater.append(i)
        else:
            smaller.append(i)
    return smaller, greater


if __name__ == "__main__":
    
    print('Question 1')
    print(divisible(8,2))       # True
    print(divisible(8,3))       # False
    print(divisible(105,3))     # True
    print(divisible(105,9))     # False
    
    print('Question 2')
    print(prime(2))             # True
    print(prime(49))            # False
    print(prime(151))           # True
    print(prime(39203))         # False
    
    print('Question 3')
    print(sum_digits(2))             # 2
    print(sum_digits(49))            # 13
    print(sum_digits(151))           # 7
    print(sum_digits(39203))         # 17
    
    print('Question 4')
    print(reverse('UTEP'))             # PETU
    print(reverse('racecar'))          # racecar
    print(reverse('W'))                # W 
    print(reverse('Week'))             # keeW 
    
    print('Question 10')
    A = np.array([2,5,7,1,2,5,7,8,9,0])
    replace_array(A,5,2302)
    print(A)                    # [   2 2302    7    1    2 2302    7    8    9    0]
    replace_array(A,5,0)
    print(A)                    # [   2 2302    7    1    2 2302    7    8    9    0]
    replace_array(A,7,-1)
    print(A)                    # [   2 2302   -1    1    2 2302   -1    8    9    0]
    replace_array(A,8,-8)
    print(A)                    # [   2 2302   -1    1    2 2302   -1   -8    9    0]
    
    print('Question 12')
    A = np.arange(25).reshape((5,5))
    print(A)
    print(diagonal_sum(A))        # 60
    print(diagonal_sum(A-12))     # 0
    B = np.array([2,5,7,1,2,7,8,9,0]).reshape((3,3))
    print(diagonal_sum(B))        # 4
    print(diagonal_sum(B+2))      # 10
    
    print('Question 19')
    Ls = [2,5,7,1,2,5,7,8,9,0]
    print(greater_than_list(Ls,4))  # [5, 7, 5, 7, 8, 9]
    print(greater_than_list(Ls,9))  # []
    print(greater_than_list(Ls,-1))  # [2, 5, 7, 1, 2, 5, 7, 8, 9, 0]
    print(greater_than_list(Ls,7))  # [8, 9]
