import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))

def treeWeight(start):
    cost = [0] * (n+1)
    dq = deque([start])
    path = [0] * (n+1)

    while dq:
        p = dq.popleft()
        for nextV, nextW in graph[p]:
            cost[nextV] = cost[p] + nextW
            path[nextV] = p
            dq.append(nextV)

    return (cost,path)

def traceback(end):
    back = end
    trace = deque()
    while back != 0:
        trace.appendleft(back)
        back = p[back]
    return trace


originC,p = treeWeight(1)
adjustC = [0] * (n+1)

for i,x in enumerate(originC):
    adjustC[i] = (x*int(len(graph[i]) == 0),i)
sortedC = sorted(adjustC, reverse=True)
max1, m1Trace = sortedC[0][0], traceback(sortedC[0][1])
max2, m2Trace = sortedC[1][0], traceback(sortedC[1][1])

i = 0
branchPoint = 0
while True:
    if i == len(m1Trace)-1 or i == len(m2Trace)-1 or m1Trace[i] != m2Trace[i]:
        branchPoint = m1Trace[i-1]
        break
    i += 1

print(originC, adjustC)
print(max1 + max2 - 2*originC[branchPoint])