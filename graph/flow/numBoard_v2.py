import sys
input = sys.stdin.readline
from collections import deque

INF = int(1e10)

def network_flow(source, sink):
    total_flow = 0

    while True:
        parent = [-1]*(nc)
        dq = deque([source])

        while dq and parent[sink] == -1:
            u = dq.popleft()
            for v in adj[u]:
                if capacity[u][v] - flow[u][v] > 0 and parent[v] == -1:
                    parent[v] = u
                    dq.append(v)

        if parent[sink] == -1:
            break

        amount = int(1e10)
        v = sink
        while v != source:
            amount = min(amount, capacity[parent[v]][v]-flow[parent[v]][v])
            v = parent[v]

        v = sink
        while v != source:
            flow[parent[v]][v] += amount
            flow[v][parent[v]] -= amount
            v = parent[v]
        total_flow += amount

    return total_flow

def add_edge(u,v,c):
    capacity[u][v] = c
    adj[u].append(v)
    adj[v].append(u)

n = int(input())
nc = n*n + n+n + 2
SRC = 0
SINK = nc-1

#1       ~ n*n     - 빈칸
#n*n+1   ~ n*n+n   - 행 합 (오른쪽 세로줄)
#n*n+n+1 ~ n*n+n+n - 열 합 (아래쪽 가로줄)

capacity = [[0]*nc for _ in range(nc)]
flow = [[0]*nc for _ in range(nc)]
ans_flow = [[0]*nc for _ in range(nc)]
adj = [[] for _ in range(nc)]
row = list(map(int,input().split()))
col = list(map(int,input().split()))
total = sum(row)

for i in range(n):
    v = n*n + i+1
    add_edge(SRC,v,row[i])
    for j in range(n):
        v2 = i*n + j+1
        add_edge(v,v2,10000)
for i in range(n):
    v = n*n + n + i+1
    add_edge(v,SINK,col[i])
    for j in range(n):
        v2 = j*n + i+1
        add_edge(v2,v,10000)

def board(cap):
    for i in range(nc):
        for j in range(nc):
            flow[i][j] = 0

    for i in range(n):
        v = n*n + i+1
        for j in range(n):
            v2 = i*n + j+1
            capacity[v][v2] = cap

    for i in range(n):
        v = n*n + n + i+1
        for j in range(n):
            v2 = j*n + i+1
            capacity[v2][v] = cap

    res = network_flow(SRC,SINK)
    if res == total:
        for i in range(nc):
            for j in range(nc):
                ans_flow[i][j] = flow[i][j]

    return res < total

def binsearch():
    lo = -1
    hi = int(1e4)

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if board(mid):
            lo = mid
        else:
            hi = mid
    return hi

print(binsearch())
for i in range(n):
    print(*ans_flow[n*n+i+1][i*n+1:i*n+n+1])