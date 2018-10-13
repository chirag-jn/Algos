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


# Fibonacci Series using Dynamic Programming (from geeksforgeeks)
def fibonacci_with_dp(n): 
      
    # Taking 1st two fibonacci nubers as 0 and 1 
    FibArray = [0, 1] 
      
    while len(FibArray) < n + 1:  
        FibArray.append(0)  
      
    if n <= 1: 
       return n 
    else: 
       if FibArray[n - 1] ==  0: 
           FibArray[n - 1] = fibonacci_with_dp(n - 1) 
      
       if FibArray[n - 2] ==  0: 
           FibArray[n - 2] = fibonacci_with_dp(n - 2) 
      
       FibArray[n] = FibArray[n - 2] + FibArray[n - 1] 
    return FibArray[n] 
      

