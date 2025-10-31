# ZADANIE 4.4------------------------------------------------------------

def fibonacci(n):
    if  not isinstance(n, int) or n<0:
        raise ValueError('Argument must be a non-negative integer.')
    
    if n==0 or n==1:
        return n
        
    a = 0
    b = 1
    for i in range(2, n+1):
        a, b=b, a+b
    return b



assert fibonacci(2)== 1
assert fibonacci(0)== 0
assert fibonacci(6)== 8
assert fibonacci(10)== 55
