n = int(input())
L = [1]

for i in range(n):
    s = 0
    for j in range(i+1):
        s += L[j]*L[i-j]
    L.append(s)

print(L[n])