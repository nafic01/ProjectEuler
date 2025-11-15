totalnum = 100
sum1 = 0
for i in range (1,totalnum+1):
    sum1 += i**2

sum2 = (sum(range(1, totalnum+1)))
answer = sum2**2-sum1
print(answer)
#print(sum2 - sum1)