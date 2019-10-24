def route_problem(cube_size):
	L = [1]*cube_size
	for i in range(cube_size):
		for j in range(i):
			print("The i :{} and the j: {}".format(i,j))
			L[j] = L[j]+L[j-1]
		L[i] = 2*L[i-1]
		print("The updated L values are :{}".format(L))
	return L[cube_size-1]

if __name__ == "__main__":
	print(route_problem(20))