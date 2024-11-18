import sys
input = sys.stdin.readline
from collections import deque

def strahler():
    res = [0]*(n+1)
    maxI = [0]*(n+1)
    dq = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            dq.append(i)
            res[i] = 1

    while dq:
        p = dq.popleft()
        for i in graph[p]:
            indegree[i] -= 1
            if res[p] > res[i]:
                res[i] = res[p]
            if res[i] == maxI[i]:
                res[i] += 1
            maxI[i] = max(maxI[i], res[p])

            if indegree[i] == 0:
                dq.append(i)

    return res


T = int(input())
for tc in range(T):
    k,n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        indegree[b] += 1

    ans = strahler()
    print(tc+1, ans[n])
