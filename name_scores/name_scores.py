alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpha_value = [x for x in range(1,27)]


def open_file(path):
	with open(path,'r') as text_file:
		string_file = text_file.readlines()

	string_file = string_file[0].split(',')
	clean_string_file = []
	for x in string_file:
		clean_string_file.append(str(x[1:-1]))
	print(clean_string_file)
	return clean_string_file[:-1]


def score_names(file):
	alpha_dict = { alpha : value  for alpha,value in zip(alphabets,alpha_value)}
	name_list = open_file(file)
	total_sum , sum = 0 , 0
	for i in range(len(name_list)):
		name = name_list[i]
		for letter in name:
			sum+= alpha_dict[letter.lower()]
		print("Sum for {} is {}".format(name,sum),end=" ")
		print(" and score for {} is {}".format(name,sum*(i+1)))
		total_sum += sum*(i+1)
		print("Updated total_score for all the names is {}".format(total_sum))
		sum = 0


if __name__ == "__main__":
	score_names('names.txt')
