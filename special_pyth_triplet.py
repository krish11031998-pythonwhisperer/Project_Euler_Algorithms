import math
import random

def pyth_theorem(a,b):
	a_sq = a*a
	b_sq = b*b
	c=math.sqrt(a_sq+b_sq)
	return c


def hundred():
	condition = True
	for a in range(1,1000):
		for b in range(1,1000):
			c = pyth_theorem(a,b)
			if (a<b<c and (a>0 and b>0) and (a<1000 and b<1000)) and condition:
				print("a:{} and b:{} c:{}".format(a,b,c))
				sum = a+b+c
				if sum == 1000:
					print("We have found the hundred pyth theorem number: a: {}, b: {}, c:{} and the sum :{}".format(a,b,c,sum))
					condition = False
				else:
					pass


if __name__ == "__main__":
	hundred()