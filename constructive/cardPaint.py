n = int(input())
L = list(map(int,input().split()))

for i in range(n-1):
    if L[i] == L[i+1]:
        print(-1)
        exit(0)

def pickDifferent(a,b):

if L[0] == 0:
    if L[1] == 0:
        L[0] = 1
    if L[1] != 0:
        L[0] = -L[1]+3

for i in range(1,n-1):
    if L[i] == 0 and L[i+1] == 0:
        L[i] = -L[i-1]+3
    if L[i] == 0 and L[i+1] != 0:
        pass

if L[n-1] == 0:
    L[n-1] = -L[n-2]+3

print(*L)