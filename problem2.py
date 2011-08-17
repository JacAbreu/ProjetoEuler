
soma_fib=2

ter1=1
ter2=2
aux=0

while ter2 <= 4000000 :
	aux=ter1
	ter1=ter2
	ter2+=aux
	if(ter2%2==0):
		soma_fib+=ter2

print (soma_fib)
