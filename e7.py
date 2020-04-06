

#def prime_factors(n):
#	factors = {1:1}
#	divisor = 2
#	while n > 1:
#		if n%divisor == 0:
#			if divisor in factors:
#				factors[divisor] += 1
#			else:
#				factors[divisor] = 1
#			n /= divisor
#		else:
#			divisor += 1
#	return factors
#
#print(prime_factors(100))

### there is an upper bound for the nth prime number n(lnn+lnlnn)>p(n)
from math import log, ceil

def find_primes(limit):
    nums = [True] * (limit + 1)
    nums[0] = nums[1] = False

    for (i, is_prime) in enumerate(nums):
        if is_prime:
            yield i
            for n in range(i * i, limit + 1, i):
                nums[n] = False

def upper_bound_for_p_n(n):
    if n < 6:
        return 100
    return ceil(n * (log(n) + log(log(n))))

def find_n_prime(n):
    primes = list(find_primes(upper_bound_for_p_n(n)))
    return primes[n - 1]

if __name__ == '__main__': 
	# driver function
	print(find_n_prime(10001))	

		

