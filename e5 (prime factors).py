# wow this takes too long. its super ineffecient.


#min_list =[]
#for num in range (2520,1000000000,1):
#	flag =0
#	for x in range(1,21,1):
#		if num%x ==0:
#			flag +=1
#		else:
#			break
##			min_list.append(num)
			
	

#print(min(min_list))




def prime_factors(n):
    factors = {1: 1}
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            if divisor in factors:
                factors[divisor] += 1
            else:
                factors[divisor] = 1
            n /= divisor
        else:
            divisor += 1
    return factors



factors_1_to_20 = []
for i in range(1, 21):
    factors_1_to_20.append(prime_factors(i))




def factors_of_range(lst):
    highest_powers = {}
    for aDict in lst:
        for (k,v) in aDict.items():
            if k not in highest_powers or highest_powers[k] < v:
                highest_powers[k] = v
	return highest_powers

factors_1_20 = factors_of_range(factors_1_to_20)
def find_lcm(aDict):
    current = 1
    for (k, v) in aDict.items():
        current *= (k ** v)
    return current

#print(find_lcm(factors_1_20))




def lcm(start, end):
    factors = []
    for i in range(start, end+1):
        factors.append(prime_factors(i))
    return find_lcm(factors_of_range(factors))

print(lcm(1, 20))

