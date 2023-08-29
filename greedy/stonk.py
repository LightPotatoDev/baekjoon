import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    L = list(map(int,input().split()))
    for i in range(n):
        L[i] = (L[i],i)

    p = 0
    profit = 0
    while p < n:
        maxVal = max(L[p:])
        v = maxVal[0]
        sell = maxVal[1]

        if sell == p:
            p += 1
        else:
            for i in range(p,sell):
                profit += v - L[i][0]
            p = sell

    print(profit)
