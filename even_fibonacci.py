"""Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
										1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""

def fib_series(num):
	if num<2:
		return num
	else:
		return(fib_series(num-1)+fib_series(num-2))


fib_nums = []
if __name__=="__main__":
	value = 0
	num = 1
	while value < 4000000:
		value = fib_series(num)
		if value < 4000000:
			fib_nums.append(value)
		num+=1
	print(fib_nums)
	even_fib_num = [x for x in fib_nums if x%2==0]
	print(even_fib_num)