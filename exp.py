print("Programme to print exp(x)")
print("Enter x :",end="")
x = int(input())

answer = 0
numerator = 1
denominator = 1

for i in range(1,60):
	term = numerator/denominator
	answer = answer + term
	numerator = numerator*x
	denominator = denominator*i
print("exp("+str(x)+") = ",answer)


