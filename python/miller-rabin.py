import math
import random

def miller_rabin(n):
	if n <= 1:
		return False
	k = 20
	s = 0
	while n % 2 == 0:
		s += 1
		d = (n - 1) / (2 ** s)
		for i in range(k):
			a = random.randint(1, n - 1)
			if math.pow(a, d) % n != 1:
				is_composite = True
				for r in range(0, s - 1):
					if math.pow(a, (2 ** r) * d) % n == 1:
						is_composite = False
						break
				if is_composite:
					return False
		n /= 2
	return True

if __name__ == "__main__":
	for i in range(2, 100):
		if miller_rabin(i):
			print(i, end=" ")
	print("")

