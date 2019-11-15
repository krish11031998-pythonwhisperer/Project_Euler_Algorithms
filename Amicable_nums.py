def div_func(num):
	proper_divisor = 0
	for x in range(num-1,0,-1):
		if num%x == 0:
			proper_divisor+=x

	if proper_divisor <= 1:
		return -1
	else:
		return proper_divisor


def dict_proper_divisor_num(limit):
	proper_div_num_dict = {}
	for x in range(2,limit):
		num = div_func(x)
		if num == -1:
			pass
		else:
			proper_div_num_dict[x] = div_func(x)

	return proper_div_num_dict


def find_amicable_pair(dict):
	amicable_pairs = set()
	d_keys = list(dict.keys())
	d_values = list(dict.values())

	for x in d_keys:
		for y in d_values:
			if x == y:
				if dict[x] == d_keys[d_values.index(y)]:
					if x == dict[x] == d_keys[d_values.index(y)] == y:
						pass
					else:
						print ("{}:{} and {}:{}".format(x,dict[x],d_keys[d_values.index(y)],y))
						amicable_pairs.add(frozenset({x,dict[x]}))
	print(amicable_pairs)
	print(len(amicable_pairs))


def amicable_num(limit):

	dict = dict_proper_divisor_num(limit)
	print(dict,sep="\n")
	# rev_dict = rev_dict_proper_divisor_num(dict)
	find_amicable_pair(dict)


if __name__ == "__main__":
	amicable_num(10000)