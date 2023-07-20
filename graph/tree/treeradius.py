import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(n-1):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))
    indegree[e] += 1

def criticalpath(start):
    visited = [0] * (n+1)
    cost = [0] * (n+1)
    path = [0] * (n+1)
    dq = deque([start])

    while dq:
        p = dq.popleft()
        if visited[p] == 1 or indegree[p] != 0:
            continue
        for nextV,nextW in graph[p]:
            newCost = cost[p] + nextW
            if newCost > cost[nextV]:
                cost[nextV] = newCost
                path[nextV] = p
                dq.append(nextV)
            indegree[nextV] -= 1
        visited[p] = 0

    return (cost,path)

def traceback(end):
    back = end
    trace = deque()
    while back != 0:
        trace.appendleft(back)
        back = p[back]
    return trace


c,p = criticalpath(1)
for i,x in enumerate(c):
    c[i] = (x,i)
sortedC = sorted(c, reverse=True)
max1, m1Trace = sortedC[0][0], traceback(sortedC[0][1])
max2, m2Trace = sortedC[1][0], traceback(sortedC[1][1])

i = 0
branchPoint = 0
while True:
    if i == len(m1Trace)-1 or i == len(m2Trace)-1 or m1Trace[i] != m2Trace[i]:
        branchPoint = m1Trace[i-1]
        break
    i += 1

print(max1 + max2 - 2*c[branchPoint][0])