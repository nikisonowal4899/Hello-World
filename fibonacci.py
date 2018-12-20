print("Programme to print first n fibbonacci number\n")
n = int(input("Enter the value of n: "))
print("First",n,"fibonacci number")

def fib(n):
	if n > 0:
		(n1,n2) = fib(n-1)
		nth = n1 + n2
		print(nth)
		return nth, n1 #returning (n-1)th and (nth) value

	else:
		print(0)
		return 0,1


fib(n-1) #calling the function for the first time


