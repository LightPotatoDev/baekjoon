from itertools import permutations

n, m = map(int,input().split())
L = list(map(int,input().split()))
permL = permutations(L,3)

num = 0
for i in list(permL):
    s = sum(i)
    if s > num and s <= m:
        num = s

print(num)