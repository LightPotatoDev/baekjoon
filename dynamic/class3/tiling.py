n = int(input())
L = [1,2]

for i in range(2,n):
    L.append(L[i-1]+L[i-2])

print(L[n-1]%10007)