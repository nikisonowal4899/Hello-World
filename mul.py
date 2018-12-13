print("This Programme will display multiplication table of a number")
print("Enter the Number :", end=" ")
n = int(input())
print("\nTable of",n)

for i in range(1, 11,):
	print(n,"x",i,"=",n*i)