
import hash_table_chain as htc

def load_factor(h):
    c = 0
    for i in range(len(h.bucket)):
        c += len(h.bucket[i])
    return c/len(h.bucket)

def longest_bucket(h):
    most = 0
    for i in range(len(h.bucket)):
        if len(h.bucket[i]) > most:
            most = len(h.bucket[i])
    return most

def check(h):
    for i in range(len(h.bucket)):
        for j in range(len(h.bucket[i])):
            if h.bucket[i][j].key%len(h.bucket) != i:
                return False
    return True

def has_duplicates(L):
    h = htc.HashTableChain(len(L))
    for i in L:
        value = h.insert(i, "")
        if value == -1:
            return True
    return False

if __name__ == "__main__":
    h = htc.HashTableChain(9)
    
    players = ['Bellinger','Betts', 'Hernandez', 'Pederson', 'Pollock', 'Taylor']
    numbers= [35, 50, 14, 31, 11, 3]

    for i in range(len(players)):
        h.insert(numbers[i],players[i])
        
    h.print_table()

    print(load_factor(h))  # 0.66666666666666
    
    print(longest_bucket(h)) # 2
    
    print(check(h)) # True
    h.bucket[2][0].key = 2302
    h.print_table()
    print(check(h)) # False
    
    L1 = [1,4,2,5,6,7,8,39,20,45]
    L2 = [1,4,2,5,6,7,8,39,20,45,9,13,5,34]
    
    
    print(has_duplicates(L1)) # False
    print(has_duplicates(L2)) # True

