from math import *

def isPrime(x):
	raiz=sqrt(x)
	for i in range(2, int(raiz)+1):
		if(x%i==0):
			return False
	return True		
	
x=600851475143
for i in range(2, int(sqrt(x))):
	if(isPrime(i)):
		while x%i==0:
			#print i
			x/=i
			aux=i

if(x<aux): print aux
else: print x

	
	
	