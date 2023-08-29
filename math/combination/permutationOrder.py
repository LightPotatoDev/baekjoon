from math import factorial

n = int(input())
L = list(map(int,input().split()))
F = [factorial(i) for i in range(n-1,0,-1)]
N = [i for i in range(1,n+1)]

if L[0] == 1:
    order = L[1]
    ans = []

    for i in F:
        x = N[(order-1) // i]
        N.remove(x)
        ans.append(x)
        order = (order-1) % i + 1

    print(*(ans+N))
else:
    P = L[1:]
    order = 0
    for i in range(n-1):
        order += F[i] * N.index(P[i])
        N.remove(P[i])
    print(order+1)

