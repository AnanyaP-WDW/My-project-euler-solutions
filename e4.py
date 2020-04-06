

palindrome_list = []
for num1 in range(1000,99,-1):
 num2=999
 while num2 > 99:
 	 product = str(num1*num2)
 	 if product == product[::-1]:
 		 palindrome_list.append(int(product))
 	 num2 = num2-1

print(palindrome_list)
#print(palindrome_list.sort())
print(max(palindrome_list))
