# ZADANIE 4.3--------------------------------------------------------

def factorial(n):
    if not isinstance(n, int) or n<0:
        raise ValueError('Argument must be a non-negative integer')
    result=1
    for i in range(2, n+1):
        result*=i
    return result



assert factorial(0) == 1
assert factorial(4)== 24
assert factorial(5) == 120