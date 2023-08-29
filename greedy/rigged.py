n = int(input())
das = int(input())
L = []
for _ in range(n-1):
    i = int(input())
    if i >= das:
        L.append(i)

if not L:
    print(0)
    exit(0)

avg = (das + sum(L)) // (len(L) + 1)
print(avg - das + 1)
