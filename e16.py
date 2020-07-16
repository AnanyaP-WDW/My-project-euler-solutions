# This is a one line I found online. It's amzing that python offers this kind of functionality
###sum(map(int, str(2**1000)))

total = 0
n = 2**1000
while n >= 1:
    total += n%10
    n /= 10

print(total)


list_of_words = ["eat","tea","ate","bat","tab","cat"]
list_of_chars = list(map(list,list_of_words))

similar = list()

for i in len(0,list_of_chars):
    for j in len(0,i):
        if list_of_chars[i].sorted() == list_of_chars[j].sorted():
            similar.append(i)
            similar.append(j)
