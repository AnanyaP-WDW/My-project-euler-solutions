def sum_natural_whole_squared(n):
	sum = ((n)*(n+1))/2
	sum = sum**2
	return sum



def sum_squared_natural_number(n):
	sum = ((n)*(n+1)*((2*n)+1))/6
	return sum

print(sum_natural_whole_squared(100) - sum_squared_natural_number(100))
