# problem 4
array = []
valid = []
factors = []
num = 100000
num = str(num)
for i in range (100000,1000000):
    i = str(i)
    if i[0] == i[-1]:
        if i[1] == i[-2]:
            if i[2] == i[-3]:
                    array.append(i)
                    
for p in array:
    p = int(p)
    for a in range(100, 1000):
        if p % a == 0:          
            b = p // a          
            if 100 <= b <= 999: 
                valid.append(p)
print(max(valid))