n = int(input())
L = [0] * (10000001)
if len(L) != 1:
    L[1] = 1
for i in range(2,n+1):
    L[i] = (L[i-1] + L[i-2])%n

print(L[n])