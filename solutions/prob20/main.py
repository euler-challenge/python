def factorial(n):
	if n < 0:
		return -1
	elif n == 0:
		return 1
	return n * factorial(n - 1)

f = str(factorial(100))
sum = 0

for i in f:
	sum += int(i)
	
print(sum)
