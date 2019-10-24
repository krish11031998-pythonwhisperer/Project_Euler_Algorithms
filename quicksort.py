"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	pivot = len(array)-1
	i = 0
	while i < len(array):
		if array[pivot] < array[i]:
			print("BEFORE: {}".format(array))
			x = array[i]
			y = array[pivot-1]
			z= array[pivot]
			array[i] = y
			array[pivot-1] = z
			array[pivot] = x
			pivot-=1
			print("AFTER: {}".format(array))
			print("*"*40)
		else:
				i+=1
				return array
	return quicksort(array)

test = [21, 4, 1, 3, 9, 20, 25, 6, 22, 14]
print(quicksort(test))