def sieve_of_Eratosthenes(n):
    list1 = [True for i in range(n)]
    sum = 0
    p = 2
    while ((p*p) < n):
        if (list1[p] == True):
            for i in range (p*p,n,p):
                list1[i] = False
        p+=1
    for p in range(2,n):
        if list1[p] == True:
            #print(p)
            sum += p
    print(sum)

if __name__ == '__main__':
    sieve_of_Eratosthenes(2000000)

