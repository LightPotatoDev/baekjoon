a,b = map(int,input().split())
L = []
n = 1
for i in range(45):
    for j in range(n):
        L.append(n)
    n += 1
print(sum(L[a-1:b]))
