# problem 2
n = 32
a = 0
b = 1
next = b  
count = 1
fibonacci = []
even_fibs = []
while count <= n:
    fibonacci.append((next))
    count += 1
    a, b = b, next
    next = a + b

for i in range (0,32):
    if fibonacci[i] % 2 == 0:
        even_fibs.append(fibonacci[i])
        
print(even_fibs)

print(sum(even_fibs))