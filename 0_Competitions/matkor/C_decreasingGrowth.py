n = int(input())
L = [0] + list(map(lambda x:int(x)*100,input().split()))

for i in range(n):
    L[i+1] += L[i]

Real = [0]*(n+1)
Real[0] = -49
growth = L[1]+98

for i in range(1,n+1):
    nxt = Real[i-1] + growth
    Real[i] = nxt

print(L)
print(Real)
print(growth)