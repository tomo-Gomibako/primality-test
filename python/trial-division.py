import math

def trial_division(n):
	# print(n)
	ret = True
	for i in range(2, int(math.sqrt(n))):
		if n % i == 0:
			ret = False
	return ret

if __name__ == "__main__":
	# print(isprime(int(input())))
	for i in range(2, 100):
		if trial_division(i):
			print(i, end=" ")
	print("")
