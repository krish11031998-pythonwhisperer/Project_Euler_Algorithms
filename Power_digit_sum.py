def product(num):
	factor_num = 2
	for i in range(num):
		factor_num*=2
		print("the number is {}".format(factor_num))
	return factor_num


def pds(factor):
	condition = True
	num = product(factor)
	numbers = []
	num_og = num
	while condition:
		remainder = num%10
		numbers.append(remainder)
		print("The appended list is :{}".format(numbers))
		num = num//10
		if num > 0:
			pass
		elif num == 0:
			condition = False
	sum = 0
	for i in numbers:
		sum+=i

	print("The number 2^{} is : {} and the sum of the digits in the number is: {}".format(factor,num_og,sum))


if __name__ == "__main__":
	pds(1000)