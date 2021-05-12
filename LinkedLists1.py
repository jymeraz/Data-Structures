import singly_linked_list as sll
import matplotlib.pyplot as plt
import math

def first(L):
    if L.head is not None:
        return L.head.data
    else:
        return -math.inf
    
def last(L):
    if L.head is not None:
        return L.tail.data
    else:
        return -math.inf

def swap_first_and_last(L):
    if L.head is None:
        return []
    if L.head.next is None:
        return L
    
    t = L.head
    while t.next.next is not None:
        t = t.next
    tail_temp = L.tail
    L.tail = t
     
    head_temp = L.head
    L.head = L.head.next
    head_temp.next = None
    
    L.tail.next = head_temp
    L.tail = L.tail.next
    
    head_temp = L.head
    L.head = tail_temp
    L.head.next = head_temp

    return L

def length(L):
    t, count = L.head, 0
    while t is not None:
        count+=1
        t = t.next
    return count

def sum_list(L):
    t, sum_l  = L.head, 0
    while t is not None:
        sum_l += t.data
        t = t.next
    return sum_l

def max_list(L):
    t, max_l  = L.head, -math.inf
    while t is not None:
        if t.data > max_l:
            max_l = t.data
        t = t.next
    return max_l

def to_list(L):
    t, python_list  = L.head, []
    while t is not None:
        python_list.append(t.data)
        t = t.next
    return python_list

def identical(L1,L2):
    t1, t2  = L1.head, L2.head
    while t1 is not None and t2 is not None:
        if t1.data != t2.data:
            return False
        t1 = t1.next
        t2 = t2.next
    return t2==None and t1==None

if __name__ == "__main__":
    plt.close('all')
    L1 = sll.List()
    L1.print()
    L1.draw()
    
    L2 = sll.List()
    L2.extend([3,6,1,0,9,7,4,8,5])
    L2.print()
    L2.draw()
    
    L3 = sll.List()
    L3.append(2)
    L3.print()
    L3.draw()
 
    print('Question 1')
    print(first(L1))   
    print(first(L2))   
    print(first(L3))   

    print('Question 2')
    print(last(L1))   
    print(last(L2))    
    print(last(L3))    

    print('Question 3')   
    swap_first_and_last(L1)
    L1.print()             
    swap_first_and_last(L2) 
    L2.print()          
    swap_first_and_last(L3) 
    L3.print()  

    L1 = sll.List()
    
    L2 = sll.List()
    L2.extend([3,6,1,0,9,7,4,8,5])

    L3 = sll.List()
    L3.append(2)

    print('Question 4')   
    print(length(L1))
    print(length(L2))
    print(length(L3))

    print('Question 5')  
    print(sum_list(L1))
    print(sum_list(L2))
    print(sum_list(L3))

    print('Question 6')
    print(max_list(L1))
    print(max_list(L2))
    print(max_list(L3))

    print('Question 7')
    print(to_list(L1))
    print(to_list(L2))
    print(to_list(L3))

    print('Question 8')
    L4 = sll.List()
    L4.extend([3,6,1,0,9,7,4,8,5])
    
    L5 = sll.List()
    L5.extend([3,6,1,0])
    
    print(identical(L1,L3))
    print(identical(L4,L2))
    print(identical(L2,L3))
    print(identical(L3,L4))
    print(identical(L4,L5))

'''
Program output
[]
[3, 6, 1, 0, 9, 7, 4, 8, 5]
[2]
Question 1
-inf
3
2
Question 2
-inf
5
2
Question 3
[]
[5, 6, 1, 0, 9, 7, 4, 8, 3]
[2]
Question 4
0
9
1
Question 5
0
43
2
Question 6
-inf
9
2
Question 7
[]
[3, 6, 1, 0, 9, 7, 4, 8, 5]
[2]
Question 8
False
True
False
False
False    
'''
