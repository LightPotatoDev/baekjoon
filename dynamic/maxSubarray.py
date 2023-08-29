import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    L = list(map(int,input().split()))

    for i in range(1,n):
        L[i] = max(L[i-1]+L[i], L[i])

    print(max(L))