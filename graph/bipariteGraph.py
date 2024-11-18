import sys
input = sys.stdin.readline

def dfs(start):
    group = [0] * (v+1)
    stk = [start]
    group[start] = 1

    while stk:
        p = stk.pop()
        for i in G[p]:
            if group[i] == 0:
                group[i] = 3-group[p]
            elif group[p] == group[i]:
                return False

            if visited[i] == 0:
                stk.append(i)
                visited[i] = 1

    return True

k = int(input())
for _ in range(k):
    v,e = map(int,input().split())
    G = [[] for _ in range(v+1)]
    for _ in range(e):
        a,b = map(int,input().split())
        G[a].append(b)
        G[b].append(a)

    visited = [0] * (v+1)
    res = "YES"
    for i in range(1,v+1):
        if visited[i] == 0:
            isBiparite = dfs(i)
            if not isBiparite:
                res = "NO"
                break
    print(res)
