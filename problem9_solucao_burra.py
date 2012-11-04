from math import *
from itertools import *


a = 3

for a in xrange(1, 1000):
	
	for b in xrange(a+1, 1000):
		
			c = 1000 - (a+b)
					
			legs = (a*a) + (b*b)
	
			hypotenuse = (c*c)
			
			if legs == hypotenuse:
				
				print "a*b*c = " +str(a*b*c)+" a ="+str(a)+" b ="+str(b) +" c ="+str(c)
				
				break
			
