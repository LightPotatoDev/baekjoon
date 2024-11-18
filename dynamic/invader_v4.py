import sys
input = sys.stdin.readline
T = int(input())

def merge(a,b):
    if L[a]+L[b] <= w:
        graph[a].add(b)
        graph[b].add(a)

def fillblocks(base):
    dp = [[-1]*5 for _ in range(n)]

    dp[0][0] = 0
    if base == 0 and (0 in graph[n]):
        dp[0][3] = 1
    if base == 1:
        dp[0][1] = 1
    if base == 2:
        dp[0][2] = 1
    if base == 3:
        dp[0][4] = 2

    for i in range(1,n):
        dp[i][0] = max(dp[i-1])
        if (i in graph[i-1]) and ((base != 1 and base != 3) or i != n-1):
            dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + 1
        if (n+i in graph[n+i-1]) and ((base != 2 and base != 3) or i != n-1):
            dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + 1
        if (i in graph[n+i]) and (base == 0 or i != n-1):
            dp[i][3] = max(dp[i-1]) + 1
        if (i in graph[i-1]) and (n+i in graph[n+i-1]) and (base == 0 or i != n-1):
            dp[i][4] = dp[i-1][0] + 2

##    for row in dp:
##        print(row)
##    print('')
    return max(dp[n-1])

def matching():
    res = 0
    res = max(fillblocks(0),res)

    if (0 in graph[n-1]):
        res = max(fillblocks(1),res)
    if (n in graph[2*n-1]):
        res = max(fillblocks(2),res)
    if (0 in graph[n-1]) and (n in graph[2*n-1]):
        res = max(fillblocks(3),res)

    return res

for _ in range(T):
    n,w = map(int,input().split())
    L = list(map(int,input().split())) + list(map(int,input().split()))

    if n == 1:
        print(2-(L[0]+L[1] <= w))
        continue

    graph = [set() for _ in range(2*n)]
    for i in range(n):
        merge(i,(i+1)%n)
        merge(i,i+n)
        merge(i+n,(i+1)%n+n)

    ans = 2*n - matching()
    print(ans)