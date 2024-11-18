import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    L = list(input().rstrip())
    n = len(str(bin(len(L)))) - 2
    ans = 'YES'

    for i in range(n):
        s = 2**i-1
        d = 2**(i+1)
        prev = -1
        for j in range(s,2**n,d):
            if L[j] == prev:
                ans = 'NO'
            prev = L[j]

    print(ans)