

from math import *
#from numeric import *
from array import array

def verificar_divi(num):
	for i in range (2, num-1):
		if(num%i==0):
			return True
	
	return False
	
def retornar_mult(num, lim):
	i=2
	mult=[]
	while((i*num)<=lim) :
		mult=mult+ [i*num]
	
	return mult
		
		
terminar.
def crivo (lim):

	#num=zeros(sqrt(lim), int)
	#num=[0]*int(sqrt(lim))
	num=[0]*lim
	num[0]=1
	num[1]=1
	for i in range (2,int(sqrt(lim))):
		if (num[i]==0):
			for j in range (2*i,lim,i): 
				num[j]=1
				
	
	return num
#print (verificar_divi(723))

crivo(80000000)

		
		