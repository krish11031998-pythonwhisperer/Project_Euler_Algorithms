import math
import numpy


def sum_of_triangle(num):
	sum = 0
	for i in range(1,num+1):
		sum+=i
	print("sum : {}".format(sum))
	print("="*10)
	return sum


def find_factor(num):
	print("Recived count value as : {}".format(num))
	factors = []
	sum = sum_of_triangle(num)
	for i in range(1,sum):
		if sum%i == 0:
			factors.append(i)
	factors.append(sum)
	print("*"*40)
	return (sum,factors)


def find_triangle(no_of_factors):
	nums = {}
	condition = False
	count = 0
	while not condition:
		count += 1
		sum,factors=find_factor(count)
		nums[count] = factors
		print("No of factors: {}".format(len(factors)))
		if len(factors) > no_of_factors:
			condition = True
	return(sum,nums[count])


if __name__=="__main__":
	print(find_triangle(50))