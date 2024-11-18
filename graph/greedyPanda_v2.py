import sys
from collections import deque
input = sys.stdin.readline

INF = 987654321
n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
graph = [[[] for _ in range(n)] for _ in range(n)]
indegree = [[0]*n for _ in range(n)]
dp = [[-INF]*n for _ in range(n)]
dy = [0,-1,0,1]
dx = [1,0,-1,0]

def inbounds(y,x):
    return 0 <= y < n and 0 <= x < n

def make_graph():
    for y in range(n):
        for x in range(n):
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if inbounds(ny,nx) and grid[y][x] < grid[ny][nx]:
                    graph[y][x].append((ny,nx))
                    indegree[ny][nx] += 1

def topo_sort():
    dq = deque()
    order = []
    for i in range(n):
        for j in range(n):
            if indegree[i][j] == 0:
                dq.append((i,j))

    while dq:
        y,x = dq.popleft()
        order.append((y,x))
        for ny,nx in graph[y][x]:
            indegree[ny][nx] -= 1
            if indegree[ny][nx] == 0:
                dq.append((ny,nx))

    return order

def find_longest_path():
    dp = [[-INF]*n for _ in range(n)]
    order = topo_sort()
    yi,xi = order[0]
    dp[yi][xi] = 1

    for y,x in order:
        for ny,nx in graph[y][x]:
            if dp[ny][nx] < dp[y][x] + 1:
                dp[ny][nx] = dp[y][x] + 1

    for r in dp:
        print(r)


make_graph()
find_longest_path()