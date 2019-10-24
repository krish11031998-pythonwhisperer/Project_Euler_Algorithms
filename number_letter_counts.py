def num_to_letters(num,limit=1000):
	letters = []
	numbers = ['one','two','three','four','five','six','seven','eight','nine']
	if num<limit:
		if num > 10 and num < 20:
			if num == 11:
				letters.append("eleven")
			elif num == 12:
				letters.append("twelve")
			elif num == 13:
				letters.append("thirteen")
			elif num >13 and num < 20:
				digit = num%10
				first_word = numbers[digit-1]
				letters.append(first_word+"teen")
		elif num >= 20 and num < 1000:
			
