import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
visited = [[0]*(n+1) for _ in range(n+1)]
match = [0]*(m+1)
graph = [0]+[list(map(int,input().split()))[1:] for _ in range(n)]

def dfs(nth_match,u):
    if visited[nth_match][u]:
        return 0
    visited[nth_match][u] = 1
    for v in graph[u]:
        if not match[v] or dfs(nth_match,match[v]):
            match[v] = u
            return 1
    return 0

def bimatch():
    match_count = 0
    for i in range(1,n+1):
        match_count += dfs(i,i)

    return match_count

print(bimatch())