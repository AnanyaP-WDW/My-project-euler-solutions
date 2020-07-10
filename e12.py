
def nth_traingleNumber(n):
    return int((n)*(n+1)/2)

def divisor(n):
    list1=[1,n]
    for i in range(2,n):
        if n%i == 0:
            list1.append(i)
    return list1

#def number_of_divisors(list):
#    if len(list) > 4:
#        return True
#    else:
#        return False

def prime_factors(n):
    dict_of_prime_factors = {}
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            if divisor in dict_of_prime_factors:
                dict_of_prime_factors[divisor] += 1
            else:
                dict_of_prime_factors[divisor] = 1
            n /= divisor
        else:
            divisor += 1
    return dict_of_prime_factors



    #number=4
    #while number_of_divisors(divisor(nth_traingleNumber(number)))== False:
        #number += 1
    #print(nth_traingleNumber(number))

def solution (n):
    dict_of_prime_factors = prime_factors(nth_traingleNumber(n))
    print(dict_of_prime_factors)
    prod = 1
    for k,v in enumerate(dict_of_prime_factors):
        prod *= (v+1)
        if prod > 100:
            print("working:Prod = {0}, number = {1} and traingle number {2}".format(prod,n,nth_traingleNumber(n)))
            print("...."),print(nth_traingleNumber(n)),print("....")
            return nth_traingleNumber(n)
        else:
            solution (n+1)

if __name__ == '__main__':
    n = 2
    solution(n)
