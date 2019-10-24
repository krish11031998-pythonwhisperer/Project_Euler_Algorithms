"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

def find_highest_factor(num):
	factors = list()
	prime_nums = prime_num(num)
	for i in prime_nums:
		if num%i==0:
			factors.append(i)

	return(max(factors))

def prime_num(num):
	prime_nums = []
	for i in range(2,num):
		condition = True
		for j in range(2,i):
				if i%j==0:
					condition = False
					print("{} % {} : {} --> condition : {}".format(i,j,i%j,condition))
		if condition:
			print("Appending {} : condition = {}".format(i,condition))
			if i not in prime_nums:
				prime_nums.append(i)
	return prime_nums


if __name__=="__main__":
	# print(prime_num(100))
	#print(find_highest_factor(13195))
	print(find_highest_factor(600851475143))