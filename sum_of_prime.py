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

def sum(num):
	sum = 0
	prime_no = prime_num(num)
	for i in prime_no:
		sum+=i
	return sum


if __name__ == "__main__":
	print(sum(2000000))