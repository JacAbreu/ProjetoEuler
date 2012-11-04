
from math import *
from itertools import *


# Formula de Euclides -> a = (m*m) - (n*n); b = 2*m*n; c = (m*m) + (n*n) 
# m = 2, n= 1 -> a = 3, b = 4, c = 5

#http://mathworld.wolfram.com/PythagoreanTriple.html
# a = m*m -1, b = 2m, c= m*m +1

def isOdd(n):
	
	if n == 1 :
		return True
	elif n%2 != 0:
		return True
	else:
		return False

m = 2
n = 1


for n in xrange (1, 1000):
	for m in xrange (n+1, 1000 - n): 
	
		print "m=" + str(m) +" n="+str(n)
	
		#conditions Euclid's formula
		if (m > n and isOdd(m-n)):
		
			aEuc = (m*m)-(n*n)
			bEuc = 2*m*n
			cEuc = (m*m)+(n*n)
		
			perimeterEuc = aEuc + bEuc + cEuc		
		
			a = m*m -1
			b = 2*m
			c = m*m +1

			perimeter = a + b + c
			
			legsEuc = (aEuc*aEuc) + (bEuc*bEuc)
	
			hypotenuseEuc = (cEuc*cEuc)
		
			legs = (a*a) + (b*b)
	
			hypotenuse = (c*c)
			
			if (perimeter == 1000 or perimeterEuc == 1000) and (legsEuc == hypotenuseEuc or legs == hypotenuse):
			
				print "m=" + str(m) +" n="+str(n)			
							
				print "a*b*c = "+str(a * b * c) + " perimeter ="+str(perimeter)
				print "aEuc*bEuc*cEuc = "+str(aEuc * bEuc * cEuc)+" perimeterEuc="+str(perimeterEuc)
			
				print "permiter " + str(perimeter) +" legs "+str(legs)+" hypotenuse "+str(hypotenuse)+" permiterEuc " + str(perimeterEuc) +" legsEuc "+str(legsEuc)+" hypotenuseEuc "+str(hypotenuseEuc)
		
				break
		
			
		else:
			
			a = m*m -1
			b = 2*m
			c = m*m +1
			
			perimeter = a + b + c
			
			legs = (a*a) + (b*b)
	
			hypotenuse = (c*c)
				
			if (perimeter == 1000) and (legs == hypotenuse):

				print "m=" + str(m) +" n="+str(n)					
											
				print "a*b*c = "+str(a * b * c)
			
				print "permiter " + str(perimeter) +" legs "+str(legs)+" hypotenuse "+str(hypotenuse)
		
				break
					
