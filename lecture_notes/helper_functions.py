import numpy as np
from math import factorial

def nPr(n, r):
    return factorial(n)/(factorial(n-r))


def nCr(n, r):
    return factorial(n)/(factorial(n-r)*factorial(r))


def enum_order_matters_no_replacement(n, r):
    
    n_new = n + r - 1
    
    return nCr(n_new, r)


def vandermonde(m, n, k):
    
    vander_sum = 0
    
    for i in range(k):
        vander_sum += nCr(m, i) * nCr(n, (k-i))
        
    return vander_sum


def Main():
    
    pass


if __name__ == '__main__':
    Main()
    