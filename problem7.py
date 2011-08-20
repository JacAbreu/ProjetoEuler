from math import *

def isPrime(x):
	raiz=sqrt(x)
	for i in range(2, int(raiz)+1):
		if(x%i==0):
			return False	
	return True		

num_pri=[0]*10001
num_pri[0]=2
num_pri[1]=3
j=5
i=2
while(i<10001):
	if(isPrime(j)):
		print ("i=",i,"j=",j)
		num_pri[i]=j
		i=i+1
		
	j=j+1
	

print(num_pri[10000])
	

	