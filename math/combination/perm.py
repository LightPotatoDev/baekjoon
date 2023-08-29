from itertools import permutations
n = int(input())
L = [i for i in range(1,n+1)]
perm = permutations(L,n)
for p in perm:
    print(*p)