#Finding factorial using recusrsive function
def factorial(n):
	if n == 1 or n == 0:
		return 1
	else:
		return n*factorial(n-1)


num = int(input("Enter a number to find its Factorial: "))
ans = factorial(num)
print("Factorial of",num,"is",ans)