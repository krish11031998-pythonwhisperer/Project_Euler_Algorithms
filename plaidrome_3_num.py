def palindrome(num):
	num_string = str(num)
	# print(type(num_string),num_string,sep="\n")
	condition = True
	for i,j in zip(range(0,len(num_string)//2),range(len(num_string)-1,len(num_string)//2-1,-1)):
		# print("i : {}".format(i,num_string[i]))
		# for j in range(len(num_string)-1,len(num_string)//2-1,-1):
		# print("j : {}".format(j,num_string[j]))
		if num_string[i]!=num_string[j] and condition:
			condition = False

	return condition


def find_palindrome():
	x =0
	y =0
	highest = 0
	for i in range(1000):
		for j in range(1000):
			value = i*j
			if palindrome(value):
				if highest < value:
					highest = value
					x = i
					y = j

	return highest,x,y




if __name__=="__main__":
	highest,num1,num2 = find_palindrome()
	print("Palindrome : {} , multiples {},{}".format(highest,num1,num2))