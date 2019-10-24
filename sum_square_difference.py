
def sum_sqaure_difference(n):
	sum_of_sqaure = 0
	sum = 0
	for i in range(n+1):
		sq = i*i
		sum_of_sqaure+=(sq)
		sum+=i
		# print("sum_of_square : {} and sum :{}".format(sum_of_sqaure,sum))

	sqaure_of_sum = sum*sum
	if sqaure_of_sum>sum_of_sqaure:
		difference = sqaure_of_sum-sum_of_sqaure
	else:
		difference = sum_of_sqaure-sqaure_of_sum
	return difference


if __name__=="__main__":
	print(sum_sqaure_difference(100))
	print(sum_sqaure_difference(100))
