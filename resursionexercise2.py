import math

def reverse(L):
    if len(L) == 0:
        return []
    return [L[-1]] + reverse(L[:-1])
# def reverse(L):
#     if len(L)==0:
#         return []
#     return reverse(L[1:]) + [L[0]]
       
def is_sorted(L):
    if len(L) <= 1:
        return True
    if L[0] > L[1]:
        return False
    return is_sorted(L[1:])

def print_binary(string_so_far,digits_left):
    if digits_left==0:
        print(string_so_far)
    else:
        print_binary(string_so_far+'0',digits_left-1)
        print_binary(string_so_far+'1',digits_left-1)
    
def permutations(word_so_far, chars_left):
    L = [] 
    if len(chars_left) == 0:
        return [word_so_far]
    else:
        for c in chars_left:
            L += permutations(word_so_far+c, chars_left.replace(c,''))
    return L
    
def meals(choice_so_far,starter,main,desert):
    if len(choice_so_far)==3:
        print(choice_so_far)
       
    if len(choice_so_far) == 0:
        for k in starter:
            meals(choice_so_far+[k],starter,main,desert)
           
    if len(choice_so_far) == 1:
        for j in main:
            meals(choice_so_far +[j],starter,main,desert)
       
    if len(choice_so_far) == 2:
        for i in desert: 
            meals(choice_so_far+[i],starter,main,desert)


if __name__ == "__main__":  
    L = [4,1,7,9,3,0,6,5,2,8]
    print(L)
    
    print('Question 1')
    print(reverse(L))
    print(reverse(L[:5]))
    print(reverse(L[5:]))
    print(reverse(L[:-2]))
    print(reverse(L[4:5]))
    print(reverse(L[5:5]))
    
    print('Question 2')
    print(is_sorted(L))
    print(is_sorted([10,20,45,77]))
    print(is_sorted([]))
    print(is_sorted([2302]))
    print(is_sorted([10,20,45,77,65]))
    
    print('Question 3')
    print_binary('',2)
    print_binary('',3)
    
    print('Question 4')
    print(permutations('','SUN'))
    print(permutations('','UTEP'))
    
    print('Question 5')
    meals([],['salad', 'soup', 'pasta'],['steak', 'fish','lasagna'], ['cake', 'ice cream'])

'''
Program Output
[4, 1, 7, 9, 3, 0, 6, 5, 2, 8]
Question 1
[8, 2, 5, 6, 0, 3, 9, 7, 1, 4]
[3, 9, 7, 1, 4]
[8, 2, 5, 6, 0]
[5, 6, 0, 3, 9, 7, 1, 4]
[3]
[]
Question 2
False
True
True
True
False
Question 3
00
01
10
11
000
001
010
011
100
101
110
111
Question 4
['SUN', 'SNU', 'USN', 'UNS', 'NSU', 'NUS']
['UTEP', 'UTPE', 'UETP', 'UEPT', 'UPTE', 'UPET', 'TUEP', 'TUPE', 'TEUP', 'TEPU', 'TPUE', 'TPEU', 'EUTP', 'EUPT', 'ETUP', 'ETPU', 'EPUT', 'EPTU', 'PUTE', 'PUET', 'PTUE', 'PTEU', 'PEUT', 'PETU']
Question 5
['salad', 'steak', 'cake']
['salad', 'steak', 'ice cream']
['salad', 'fish', 'cake']
['salad', 'fish', 'ice cream']
['salad', 'lasagna', 'cake']
['salad', 'lasagna', 'ice cream']
['soup', 'steak', 'cake']
['soup', 'steak', 'ice cream']
['soup', 'fish', 'cake']
['soup', 'fish', 'ice cream']
['soup', 'lasagna', 'cake']
['soup', 'lasagna', 'ice cream']
['pasta', 'steak', 'cake']
['pasta', 'steak', 'ice cream']
['pasta', 'fish', 'cake']
['pasta', 'fish', 'ice cream']
['pasta', 'lasagna', 'cake']
['pasta', 'lasagna', 'ice cream']
'''
