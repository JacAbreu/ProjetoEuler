#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.


#by @juanplopes => mmc(a, b) = a*b/MDC(a, b)

from math import *
from array import array
from itertools import *


for val in count(1):

	if not any(val % i for i in range(1, 21) ):
		
		print val

		break




		



