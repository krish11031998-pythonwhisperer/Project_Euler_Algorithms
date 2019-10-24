def odd_num(num):
	num = (3*num)+1
	return num

def even_num(num):
	num = num//2
	return num


def rec_collatz(num,numbers):
	if num>1:
		if num%2 == 0:
			num = even_num(num)
		else:
			num = odd_num(num)
		numbers.append(num)
		return rec_collatz(num,numbers)
	else:
		return numbers

def collatz_nums():
	numbers_dict = {}
	highest_num = 0
	longest_chain_num = 0

	for i in range(13,1000000):
		numbers= []
		numbers.append(i)
		try:
			rec_collatz(i,numbers)
		except RecursionError:
			print("Couldn't find the collatz sequence for: {}".format(i))
		else:
			numbers_dict[i] = numbers
			if len(numbers) > longest_chain_num:
				highest_num = i
				longest_chain_num = len(numbers)

	return(highest_num,longest_chain_num,numbers_dict[highest_num])

if __name__ == "__main__":
	print(collatz_nums())
