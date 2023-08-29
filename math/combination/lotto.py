from itertools import combinations

while True:
    inp = list(map(int,input().split()))
    if len(inp) == 1:
        break

    L = inp[1:]
    comb = combinations(L,6)
    for c in comb:
        print(*c)
    print('')