import matplotlib.pyplot as plt
import numpy as np
import min_heap

def is_heap(L):
    k = 1
    while k < len(L):
        if L[k] < L[(k-1)//2]:
            return False
        k += 1
    return True

def second(H):
    if len(H.heap) < 2:
        return None
    
    left = H.heap[1].key
    if len(H.heap) > 2:
        right = H.heap[2].key
    else:
        return left
    
    if left < right:
        return left
    else: 
        return right

def height(H):
    count = 0
    i = 0
    while (2*i + 1) < len(H.heap):
        i = 2*i + 1
        count += 1
    return count

def height1(H):
    return int(np.log2(len(H.heap)))

def path(H,k):
    if k == 0:
        return [H.heap[0].key]
    return [H.heap[k].key] + path(H,((k-1)//2))

def equal_siblings(H):
    k = 0
    while k < len(H.heap):
        if (2*k + 2) < len(H.heap):
            if H.heap[(2*k + 1)].key ==  H.heap[(2*k + 2)].key:
                return True
        k += 1
    return False

if __name__=="__main__":
    plt.close('all')
    L0 = [1, 2, 3, 4, 5, 1]
    L1 = [i for i in range(10)]
    L2 = [2302]
    L3 = []
    L4 = [1, 2, 3, 4, 5, 3]
    L5 = [2, 2]
    L6 = [ 2, 2, 1]
    print('-- is_heap')
    for L in [L0,L1,L2,L3,L4,L5,L6]:
        print(is_heap(L))
    
    H1 = min_heap.MinHeap()
    for i in [4,8,2]:
        H1.insert(i)
    H1.draw()
    H2 = min_heap.MinHeap()
    for i in [4,8,9,14,5,7]:
        H2.insert(i)
    H2.draw()
    H3 =  min_heap.MinHeap()
    for i in [4,6,11,8,9,14,5,0,3,7,4]:
        H3.insert(i)
    H3.draw()
    
    H4 =  min_heap.MinHeap()
    for i in [5,0,3,7,8,9,14,4,6,8,9,14,5,6,7,6]:
        H4.insert(i)
    H4.draw()
    
    print('-- second')
    for H in [H1,H2,H3,H4]:
        print(second(H))
        
    print('-- height')
    for H in [H1,H2,H3,H4]:
        print(height(H))
        
    print('-- height1')
    for H in [H1,H2,H3,H4]:
        print(height1(H))    
     
    print('-- path')
    for i in [0,2,4,12,15]:
        print(path(H4,i))    
        
    print('-- equal_siblings')
    for H in [H1,H2,H3,H4]:
        print(equal_siblings(H)) 
        
    # H4 =  min_heap.MinHeap()
    # H4.insert(1)
    # H4.insert(2)
    # H4.insert(0)
    # H4.draw()
    # print('test', second(H4))
     
'''
Program output
-- is_heap
False
True
True
True
True
True
False
-- second
4
5
3
3
-- height
1
2
3
4
-- height1
1
2
3
4
-- path
[0]
[3, 0]
[8, 4, 0]
[9, 5, 3, 0]
[7, 6, 5, 4, 0]
-- equal_siblings
False
False
True
True        
'''   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
