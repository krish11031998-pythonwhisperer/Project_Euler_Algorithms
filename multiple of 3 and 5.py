"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""

def sum_of_multiple(limit,num1=3,num2=5):
	sum = 0
	for i in range(1,limit):
		if (i%num1 == 0) or (i%num2==0):
			print(i,end="\t")
			sum+=i
	print()
	print("*"*40)
	print("Sum of all the {} and {} multiples is = {}".format(num1,num2,sum))


if __name__ == "__main__":
	sum_of_multiple(100)