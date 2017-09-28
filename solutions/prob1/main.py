def factorial(n):
	if n < 0:
		return -1
	elif n == 0:
		return 1
	return n * factorial(n - 1)
	
f = str(factorial(100))
s = 0

for i in f:
	s += int(i)

print(s)
