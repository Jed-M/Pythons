import math









'''def adding(n,m):
    if n <= 1:
        return 1 
    else:
        return n + adding(n - 1)
    
print(adding([5,6,7,8,9,10,16,42],4))'''
        

def add(n):
    if n <= 1:
        return n
    else:
        return n + add(n-1)
    
print(add(5))
        
