import math

mini = int(input())
maxi = int(input())
L = []

def isprime(num):
    if num == 1: return 0

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: return 0

    return num

for i in range(mini, maxi + 1):
    L.append(isprime(i))

if sum(L) == 0:
    print(-1)
else:
    print(sum(L))
    print(min([i for i in L if i != 0]))