L = list(map(int,input().split()))
L.sort()

if L[2] >= L[1] + L[0]:
    L[2] = L[1] + L[0] - 1
print(sum(L))