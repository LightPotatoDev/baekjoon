n, m = map(int, input().split())
L = [i for i in range(1,n+1)]

for _ in range(m):
    b1, b2 = map(int, input().split())
    L[b1-1], L[b2-1] = L[b2-1], L[b1-1]
print(' '.join(map(str,L)))
