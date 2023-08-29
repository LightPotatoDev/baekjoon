n,m,k = map(int,input().split())
L = [list(input()) for _ in range(n)]
for i in L:
    i.sort()
L.sort()

A = []
for i in range(k):
    A.extend(L[i])
A.sort()
print(''.join(A))