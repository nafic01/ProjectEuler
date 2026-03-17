primes = []

# 1) We start from 2, the first prime number, and check each number up to 2 million for prime
for i in range(2, 2000001):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
print(sum(primes))
    
# 2) We can also use the Sieve of Eratosthenes to find all prime numbers up to 2 million more efficiently
sieve = [True] * 2000001
sieve[0] = sieve[1] = False  # 0 and 1 as they are not prime numbers

for i in range (2, int(2000001**0.5) + 1):
    if sieve[i]:
        for j in range(i * i, 2000001, i):
            sieve[j] = False
num = 0

for i in range(2000001):
    if sieve[i]:
        num += i
print(num)