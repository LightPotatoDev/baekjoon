from itertools import combinations
from collections import deque

n = int(input())
ppl = list(map(int,input().split()))
totalPpl = sum(ppl)
graph = [[] for _ in range(n+1)]
for i in range(n):
    graph[i+1] = list(map(int,input().split()))[1:]

def bfs(L):
    picked = [0]*(n+1)
    for i in L:
        picked[i] = 1

    visited = [0]*(n+1)
    visited[L[0]] = 1
    dq = deque([L[0]])

    while dq:
        p = dq.popleft()

        for i in graph[p]:
            if picked[i] == 1 and visited[i] == 0:
                visited[i] = 1
                dq.append(i)

    for i in L:
        if visited[i] == 0:
            return False
    return True

def getPpl(L):
    s = 0
    for i in L:
        s += ppl[i-1]
    another = totalPpl - s
    return abs(another - s)

ans = int(1e8)
N = list(range(1,n+1))
for i in range(1,n):
    comb = combinations(N,i)
    for A in comb:
        B = list(set(N) - set(A))
        if bfs(A) and bfs(B):
            ans = min(ans,getPpl(A))

if ans == int(1e8):
    print(-1)
else:
    print(ans)