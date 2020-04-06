

def pythagorean_trips_upto_sum():
	for a in range(1,332):
		for b in range(2,449):
			for c in range(3,997):
				if((a+b+c) == 1000 and (a**2 + b**2)== c**2):
					return a,b,c


if __name__ == '__main__':
	a,b,c=pythagorean_trips_upto_sum()
	print(a,b,c)
	print(a*b*c)


## decent result:
# I actually think mine is better due to less compute
# def pythagorean_triplet(a, b, c):
#    if a ** 2 + b ** 2 == c ** 2:
#        return True
#    else:
#        return False


#for a in range(1, 1000):
#    for b in range(a, 1000 - a):
#        for c in range(b, 1000 - b):
#            if a + b + c == 1000:
#                if pythagorean_triplet(a, b, c):
#                    print('{}^2 + {}^2 = {}^2'.format(a, b, c))
#                    print('{} + {} + {} = 1000'.format(a, b, c))
#                    print('Product is {}'.format(a * b * c))