def merge_sort(input_array):
	if len(input_array) > 1:
		middle = len(input_array)//2
		L = input_array[:middle]
		R = input_array[middle:]

		merge_sort(L)
		merge_sort(R)

		i=j=k=0

		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				input_array[k] = L[i]
				i+=1
			else:
				input_array[k] = R[j]
				j+=1
			k+=1

		while i < len(L):
			input_array[k] = L[i]
			i+=1
			k+=1

		while j < len(R):
			input_array[k] = R[j]
			j+=1
			k+=1

	else:
		pass
	return input_array


if __name__ == "__main__":
	print(merge_sort([3,45,20,425,31,3252,43634,43,21,22,5,66,1]))
