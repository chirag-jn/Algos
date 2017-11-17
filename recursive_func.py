def gcd(a,b):
	temp=b
	b=a%b
	if b==0:
		return temp
	else:
		return gcd(temp,b)

def fact(n):
	if n==1:
		return n
	else:
		return n*(fact(n-1))

def sum_digits(n):
	if(n==0):
		return 0
	else:
		return (n%10) +sum_digits(n//10)

def fibonacci(n):
	if(n<=1):
		return n
	else:
		return (fibonacci(n-1)+fibonacci(n-2))

def fibonacci_run():
	# n: number of terms
	for i in range(int(input())):
		print(fibonacci(i))

