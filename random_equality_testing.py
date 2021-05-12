import math 
import time
from numpy import *

def equal_functions_int(f1,f2):
    for i in range(500):
       x = random.randint(10000)-5000
       if eval(f2) != eval(f1):
           return False
    return True

def equal_functions_float(f1,f2):
    for i in range(500):
       t = (random.rand()-0.5)*2*math.pi
       if abs(eval(f2)-eval(f1))>(10**-5):
           return False
    return True

if __name__ == "__main__":  
    random.seed(0)
    
    f1 = 'x*x + x - 12'
    f2 = '(x+4)*(x-3)'
    f3 = '(x+4)*(x+3)'
    f4 = 'x%11 +1'
    f5 = '(x+1)%11'
    
    f6 = 'tan(t)+1'
    f7 = 'max(.95,sin(t))'
    f8 = 'max(.95,cos(t))'
    f9 = 'sin(t)**2 + cos(t)**2 - 1'
    f10 = 'sin(t)*(1/cos(t) + 1/sin(t))'
    
    # print('Integer functions')    
    # for i in range(5):
    #     x = random.randint(1000)-500
    #     for f in [f1,f2,f3,f4,f5]:
    #         y = eval(f)
    #         print('function: y = {}; x = {}; y = {} '.format(f,x,y))
    #     print()     
       
        
    # print('Floating point functions')    
    # for i in range(5):
    #     t = (random.rand()-0.5)*2*math.pi   
    #     for f in [f6,f7,f8,f9,f10]:
    #         y = eval(f)
    #         print('function: y = {}; t = {:10.5f}; y = {:10.8f} '.format(f,t,y))
    #     print()          
      
    for f11 in [f1,f2,f3,f4,f5]:
        for f12 in [f1,f2,f3,f4,f5]:
            print(f11+' == '+f12,':',equal_functions_int(f11,f12))
    print() 
    for f1 in [f6,f7,f8,f9,f10]:
        for f2 in [f6,f7,f8,f9,f10]:
            print(f1+' == '+f2,':',equal_functions_float(f1,f2))
    
