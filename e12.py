
def nth_traingleNumber(n):
    return int((n)*(n+1)/2)

def divisor(n):
    list1=[1,n]
    for i in range(2,n):
        if n%i == 0:
            list1.append(i)
    return list1

def number_of_divisors(list):
    if len(list) > 4:
        return True
    else:
        return False

if __name__ == '__main__':
    number=4
    while number_of_divisors(divisor(nth_traingleNumber(number)))== False:
        number += 1
    print(nth_traingleNumber(number))
