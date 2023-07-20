from itertools import combinations

T = int(input())

for _ in range(T):
    n = int(input())
    L = input().split()

    if n >= 33:
        print(0)
        continue

    comb = combinations(L,3)
    dist = []
    for i in comb:
        d = 0
        for j in range(-1,2):
            d += len(set(i[j])|set(i[j+1])) - 4
        dist.append(d)
    print(min(dist))