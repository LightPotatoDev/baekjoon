from itertools import product

for n in range(2,15):
    prod = product([1,-1,2,-2], repeat=n)
    s = 4**n
    for p in prod:
        for i in range(n):
            if p[i-1] + p[i] == 0:
                s -= 1
                break

    print(s)

