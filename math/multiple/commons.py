n, k = map(int,input().split())
L = []

for i in range(1, n+1):
    if n%i == 0:
        L.append(i)

try:
    print(L[k-1])
except:
    print(0)