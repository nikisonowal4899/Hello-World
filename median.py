print("Enter a string of Numbers with commas : ",end="")
s = input() #taking number as string
data = s.split(",")
print("String of number =",data)
l = len(data)

for i in range(0,l):
	data[i] = int(data[i]) #converting string to integer
data.sort() #sorting the array
print("Sorted list of number",data)

if l%2 == 1: #odd no. of elements
	medianPos = (l-1)/2
	median = data[int(medianPos)]
else: #even no. of elements
	upperMedianPos = l/2
	lowerMedianPos = upperMedianPos - 1
	median = (data[int(upperMedianPos)] + data[int(lowerMedianPos)])/2

print("Median of the given data = ",median)