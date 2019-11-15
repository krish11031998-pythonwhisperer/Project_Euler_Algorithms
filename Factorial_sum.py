
def factorial_num(num):
	prod = 1
	for x in range(1,num+1):
		prod*=x
	prod_string = str(prod)
	print(prod_string)
	return sum_of_digits(prod_string)

def sum_of_digits(num_string):
	sum = 0
	for i in num_string:
		sum+= int(i)
	return sum

if __name__ == '__main__':
	print(factorial_num(100))