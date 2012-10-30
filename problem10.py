#Find the sum of all the primes below two million.

from math import *


def isPrime(x):
    raiz=sqrt(x)
    for i in range(2, int(raiz)+1):
        
        if(x%i==0):
            return False
            
            
x = 2000000
sum_primes = 0
for i in range(2, x):

    if(isPrime(i) != False):
    
        sum_primes = sum_primes + i        
        



print "------"

print sum_primes

#answer 142913828922
