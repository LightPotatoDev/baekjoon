n,m = map(int,input().split())
L = []
for _ in range(n):
    L.append(list(map(int,input().split())))

area = 2*n*m

def calcSurface(A):
    a = 0
    lastH = 0
    for h in A:
        if h > lastH:
            a += (h-lastH)
        lastH = h
    return a

for i in range(n):
    area += calcSurface(L[i])
    area += calcSurface(L[i][::-1])

for c in range(m):
    A = []
    for r in range(n):
        A.append(L[r][c])
    area += calcSurface(A)
    area += calcSurface(A[::-1])

print(area)
