n = int(input())

D = dict()
for _ in range(n):
    a,b = input().split()

    if a not in D:
        D[a] = 0
    if b not in D:
        D[b] = 0

    if a == 'ChongChong' or b == 'ChongChong' or any([D[a],D[b]]) == 1:
        D[a],D[b] = 1,1

print(sum(D.values()))