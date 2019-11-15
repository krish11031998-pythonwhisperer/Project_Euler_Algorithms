pyramid_nums = '75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'
# pyramid_nums = '3 7 4 2 4 6 8 5 9 3'

def find_max_arr(arr2,index):
	highest = 0
	for x in range(index,index+2):
		if arr2[x] > highest:
			highest = arr2[x]
			index = x
		else:
			pass
	return highest,index

def find_sum_max(arr):
	sum = 0
	for x in arr:
		sum+=x
	return sum

def find_max_pyramid(pyramid_arr):
	max_num_arr = [pyramid_arr[0]]
	index = 0
	for x in range(1,len(pyramid_arr)):
		max_num, index = find_max_arr(pyramid_arr[x],index)
		max_num_arr.append(max_num)
	sum = find_sum_max(max_num_arr)
	return max_num_arr,sum

def pyramid_arr(steps):
	pyramid_nums_split = pyramid_nums.split(' ')
	print(pyramid_nums_split)
	pyramid_nums_arr = [int(pyramid_nums_split[0])]
	counter = 1
	for x in range(2,steps+1):
		temp_arr = []
		for y in range(counter,counter+x):
			temp_arr.append(int(pyramid_nums_split[y]))
		pyramid_nums_arr.append(temp_arr)
		counter+=x


	print(pyramid_nums_arr)

	length_pyramid = [1]

	for x in range(1,len(pyramid_nums_arr)):
		length_pyramid.append(len(pyramid_nums_arr[x]))

	print(length_pyramid)

	return find_max_pyramid(pyramid_nums_arr)



if __name__ == '__main__':
	max_num_arr , sum = pyramid_arr(steps=15)
	print("The max num_arr and sum is {} and {}".format(max_num_arr,sum))






