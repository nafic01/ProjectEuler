# problem 3
import math
factors = []
n = 600851475143
i = 2
while i <= math.sqrt(600851475143):
    while n % i == 0:
         factors.append(i)
         n = n // i
    i = i+1
print(max(factors))