#Find the sum of the digits in the number 100!

from math import *

def factorial (n):
	if n == 0:
		return 1
	else:
		return n*factorial(n-1)
		
result = factorial(100)

sum_digits_factorial_100 = 0

result_aux = result
while(result_aux > 0):

	sum_digits_factorial_100 += result_aux % 10
	
	result_aux /=10
	
print sum_digits_factorial_100

