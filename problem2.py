
soma_fib=2
termo1=1
termo2=2

while termo2 <= 4000000 :
	termo1,termo2=termo2,termo2+termo1 
	if(termo2%2==0):
		soma_fib+=termo2

print (soma_fib)
