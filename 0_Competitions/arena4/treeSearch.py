import sys
input = sys.stdin.readline
from collections import deque

n,q = map(int,input().split())
graph = [[] for _ in range(n+1)]
toggled = [0]*(n+1)
toggled[1] = 1

for i in range(n):
    graph[i+1] = list(map(int,input().split()))[-1:0:-1]

def dfs():
    visited = [0] * (n+1)
    vList = []
    stk = [1]

    while stk:
        p = stk.pop()
        if visited[p] == 0:
            visited[p] = 1
            vList.append(p)
            if toggled[p] == 1:
                stk.extend(graph[p])
    return vList

cursor = dfs()[1]
for _ in range(q):
    cmd = input().rstrip().split()

    if (cmd[0] == 'toggle'):
        toggled[cursor] = 1 - toggled[cursor]
    if (cmd[0] == 'move'):
        struct = dfs()
        pos = struct.index(cursor)
        diff = int(cmd[1])
        if diff < 0:
            pos = max(1,pos+diff)
        else:
            pos = min(len(struct)-1,pos+diff)
        cursor = struct[pos]
        print(cursor)
