from itertools import product

choices = range(0,10)
perm = product(choices, repeat=6)

n = int(input())
const = (100001,10001,1001,101,11,2)
const2 = (100000,10000,1000,100,10,1)

has_div = False

for i in list(perm):
    num = 0
    for j in range(6):
        num += const[j] * i[j]
    if num == n:
        result = 0
        for k in range(6):
            result += const2[k] * i[k]
        print(result)
        has_div = True
        break

if has_div == False:
    print(0)

