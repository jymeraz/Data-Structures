import singly_linked_list as sll
import matplotlib.pyplot as plt
import math

def count(L,x):
    t, c  = L.head, 0
    while t != None:
        if t.data == x:
            c+=1
        t = t.next
    return c

def sum_first_n(L,n):
    t, s  = L.head, 0
    count = 0
    while t != None and count < n:
        s += t.data
        count += 1
        t = t.next
    return s

def add_n(L,n):
    t = L.head
    while t != None:
        t.data += n
        t = t.next
    
def is_sorted(L):
    t = L.head
    while t != None:
        if t.next != None:
            if t.data > t.next.data:
                return False
        t = t.next
    return True
    
def insert_head(L,x):
    new_head = sll.ListNode(x)
    new_head.next = L.head
    L.head = new_head
    return
    
def remove_first(L):
    if L.head != None:
        L.head = L.head.next
    return
            
def remove_last(L):
    if L.head == None:
        return
    if L.head.next == None:
        L.head = None
        return
    
    t = L.head
    while t.next.next != None:
        t = t.next
    L.tail = t
    L.tail.next = None
    return
    
def remove(L,x):
    t = L.head
    previous = L.head
    found = False
    while t != None and not found:
        if t.data == x:
            if t == L.head:
                L.head = L.head.next
            found = True
            previous.next = t.next
        previous = t
        t = t.next
    return

if __name__ == "__main__":
    plt.close('all')
    L1 = sll.List()
    L1.print()
    L1.draw()
    
    L2 = sll.List()
    L2.append(2)
    L2.print()
    L2.draw()
    
    L3 = sll.List()
    L3.extend([3,6,1,4,0,9,7,4,8,5,9,7,9])
    L3.print()
    L3.draw()
    
    print('Question 1')
    print(count(L1,2)) 
    print(count(L2,2)) 
    print(count(L3,2)) 
    print(count(L3,4)) 
    print(count(L3,9)) 
    
    print('Question 2')
    print(sum_first_n(L1,2))
    print(sum_first_n(L2,2))
    print(sum_first_n(L3,0))      
    print(sum_first_n(L3,6))   
    print(sum_first_n(L3,10)) 
    
    print('Question 3')   
    add_n(L1,3)
    L1.print()
    add_n(L2,4)
    L2.print()
    add_n(L3,5)
    L3.print()
    add_n(L3,1)
    L3.print()
    
    L1 = sll.List()
    L2 = sll.List()
    L2.append(2)
    L3 = sll.List()
    L3.extend([3,6,1,4,0,9,7,4,8,5,9,7,9])
    L4 = sll.List()
    L4.extend([2,3,6,7,8,9])
    L5 = sll.List()
    L5.extend([2,3,6,7,8,9,0])
    
    
   
    print('Question 4')   
    print(is_sorted(L1))
    print(is_sorted(L2))
    print(is_sorted(L3))
    print(is_sorted(L4))
    print(is_sorted(L5))
    
    print('Question 5')  
    L1 = sll.List()
    L2 = sll.List()
    L2.append(2)
    L3 = sll.List()
    L3.extend([3,6,1,4,0,9,7,4,8,5,9,7,9])
    L4 = sll.List()
    L4.extend([2,3,6,7,8,9])
    L5 = sll.List()
    L5.extend([2,3,6,7,8,9,0])
    
    insert_head(L1,3)
    L1.print()
    insert_head(L2,4)
    L2.print()
    insert_head(L3,5)
    L3.print()
    insert_head(L4,1)
    L4.print()
    insert_head(L5,1)
    L5.print()
    
    print('Question 6')
    remove_first(L1)
    L1.print()
    remove_first(L2)
    L2.print()
    remove_first(L3)
    L3.print()
    remove_first(L4)
    L4.print()
    remove_first(L5)
    L5.print()
    
    print('Question 7')
    remove_last(L1)
    L1.print()
    remove_last(L2)
    L2.print()
    remove_last(L3)
    L3.print()
    remove_last(L4)
    L4.print()
    remove_last(L5)
    L5.print()

    L2.append(2)
    print('Question 8')
    remove(L1,5)
    L1.print()
    remove(L2,2)
    L2.print()
    remove(L3,0)
    L3.print()
    remove(L4,2)
    L4.print()
    remove(L5,9)
    L5.print()

'''
[]
[2]
[3, 6, 1, 4, 0, 9, 7, 4, 8, 5, 9, 7, 9]
Question 1
0
1
0
2
3
Question 2
0
2
0
23
47
Question 3
[]
[6]
[8, 11, 6, 9, 5, 14, 12, 9, 13, 10, 14, 12, 14]
[9, 12, 7, 10, 6, 15, 13, 10, 14, 11, 15, 13, 15]
Question 4
True
True
False
True
False
Question 5
[3]
[4, 2]
[5, 3, 6, 1, 4, 0, 9, 7, 4, 8, 5, 9, 7, 9]
[1, 2, 3, 6, 7, 8, 9]
[1, 2, 3, 6, 7, 8, 9, 0]
Question 6
[]
[2]
[3, 6, 1, 4, 0, 9, 7, 4, 8, 5, 9, 7, 9]
[2, 3, 6, 7, 8, 9]
[2, 3, 6, 7, 8, 9, 0]
Question 7
[]
[]
[3, 6, 1, 4, 0, 9, 7, 4, 8, 5, 9, 7]
[2, 3, 6, 7, 8]
[2, 3, 6, 7, 8, 9]
Question 8
[]
[]
[3, 6, 1, 4, 9, 7, 4, 8, 5, 9, 7]
[3, 6, 7, 8]
[2, 3, 6, 7, 8]
'''