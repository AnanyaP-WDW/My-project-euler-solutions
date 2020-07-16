total = 0
for i in range(100,1000000):
    n = i
    temp_total = 0
    while n > 1:
        if n%2 == 0:
            temp_total += 1
            n /= 2
        else:
            temp_total += 1
            n = 3*n + 1
        if n ==1:
            temp_total += 1
            break
    if temp_total > total:
        total = temp_total
        number_longest = i

print(total,number_longest)
