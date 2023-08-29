import math

L = [0]*9
n = list(map(int,list(input())))
for i in n:
    if i == 9 or i == 6:
        L[6] += 1
    else:
        L[i] += 2

print(math.ceil(max(L)/2))