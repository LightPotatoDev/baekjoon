import sys
input = sys.stdin.readline

n,m,a,b,c = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s].append((w,e))
    graph[e].append((w,s))

ans = int(1e8)
def traverse(cur,visited,cost,maxcost):
    global ans
    if cost > c:
        return
    if cur == b:
        ans = min(ans,maxcost)
        return
    for w,nxt in graph[cur]:
        if visited[nxt] == 0:
            visited[nxt] = 1
            traverse(nxt,visited,cost+w,max(w,maxcost))
            visited[nxt] = 0

traverse(a,[0]*(n+1),0,0)
if ans == int(1e8):
    print(-1)
else:
    print(ans)