while 1:
	num = int(input("Prime factors of:\n"))
	prime_div = []
	div = 6
	while num > 1:
		while num % 2 == 0: prime_div.append(2); num /= 2
		while num % 3 == 0: prime_div.append(3); num /= 3
		while num % (div - 1) == 0: prime_div.append(div - 1); num /= div - 1
		while num % (div + 1) == 0: prime_div.append(div + 1); num /= div + 1
		div += 6
	print(prime_div)
