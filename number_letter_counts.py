def numbers(num):
	numbers_split_rev = []
	while num>0:
		numbers_split_rev.append(num%10)
		num //=10
	num_split = [numbers_split_rev[x] for x in range(len(numbers_split_rev)-1,-1,-1)]
	return nums_to_letters(num_split , len(num_split))

def nums_to_letters(num_arr,length):
	last_two_digits = ""
	rest_digits = ""
	numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
	tens_nums = ['-',['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'],'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
	if len(num_arr) == 1:
		rest_digits+= numbers[num_arr[0]]
	elif len(num_arr) >=2:
		num_tens , num_ones = tuple(num_arr[-2:])
		print("The last two digits is {} and {}".format(num_tens,num_ones))
		if num_tens ==1:
			last_two_digits = tens_nums[num_tens][num_ones]
		elif num_tens >1:
			if num_ones >=1 and num_ones < 10:
				last_two_digits = tens_nums[num_tens] + numbers[num_ones]
			elif num_ones == 0 and num_tens != 0:
				last_two_digits = tens_nums[num_tens]
		elif num_tens == 0 and num_ones != 0:
			last_two_digits = numbers[num_ones]
		else:
			pass

		if len(num_arr)>2:
			if len(num_arr[:-2]) ==2 :
				for x in range(len(num_arr[:-2])):
					if (num_arr[x]>=1 and num_arr[x]<=9) and x == 0:
						rest_digits += numbers[num_arr[x]] + 'thousand'
					elif (num_arr[x]>=1 and num_arr[x]<=9) and x == 1:
						rest_digits += numbers[num_arr[x]] + 'hundredand'
			elif len(num_arr[:-2]) ==1:
				if (num_arr[0]>=1 and num_arr[0]<=9):
					if last_two_digits == '':
						rest_digits += numbers[num_arr[0]] + 'hundred'
					else:
						rest_digits += numbers[num_arr[0]] + 'hundredand'



	rest_digits+= last_two_digits

	print(len(rest_digits),rest_digits,sep=" ",end= '\n'+'*'*10+'\n')
	return(len(rest_digits))


if __name__ == '__main__':

	length_of_all = 0
	for x in range(1,1001):
		length_of_all += numbers(x)

	print(length_of_all)