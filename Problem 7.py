# Problem 7
prime = [2]

temp = False

for i in range(1,500000):
    if i % 2 != 0:
        for y in range(2,i):
            if i % y == 0:
                temp = False
                break
            else:
                temp = True
        if temp == True:
            prime.append(i)
    if len(prime) == 10002:
        break
            
print(prime)
print(prime[10000])
