n = int(input())
L = [0] * (n)
L[0] = 1
if len(L) != 1:
    L[1] = 1

for i in range(2,n):
    L[i] = L[i-1] + L[i-2]

print(L[n-1])