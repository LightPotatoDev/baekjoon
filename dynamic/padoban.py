T = int(input())

for _ in range(T):
    L = [1,1,1]
    n = int(input())
    for i in range(3, n):
        L.append(L[i-2]+L[i-3])

    print(L[n-1])