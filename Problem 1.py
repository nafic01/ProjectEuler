# problem 1
square = []
temp = 0
for i in range (0,240000):
    square.append(i**2)

for x in range (240000):
    if square[x] % 2 != 0:
        temp += square[x]
print(temp)

# Solution 2
print(sum([n**2 for n in range(240000) if n % 2 == 1 ]))


# Solution 3
print(sum([n for n in range(1000) if n % 3 == 0 or n % 5 == 0]))









    
