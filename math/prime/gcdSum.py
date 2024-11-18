import math

T = int(input())

for _ in range(T):
    L = list(map(int,input().split()[1:]))
    n = len(L)
    ans = 0
    for i in range(n-1):
        for j in range(i+1,n):
            ans += math.gcd(L[i],L[j])

    print(ans)
