L = [1,1,2,4]
for i in range(4,70):
    L.append(L[i-4]+L[i-3]+L[i-2]+L[i-1])

T = int(input())
for _ in range(T):
    n = int(input())
    print(L[n])