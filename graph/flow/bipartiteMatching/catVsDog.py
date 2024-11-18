import sys
input = sys.stdin.readline

def dfs(nth_match,u):
    if visited[nth_match][u]:
        return 0
    visited[nth_match][u] = 1
    for v in graph[u]:
        if match[v] == -1 or dfs(nth_match,match[v]):
            match[v] = u
            return 1
    return 0

def bimatch():
    match_count = 0
    for i in range(n):
        match_count += dfs(i,i)

    return match_count

t = int(input())
for _ in range(t):
    c,d,view = map(int,input().split())
    visited = [[0]*view for _ in range(view)]
    match = [-1]*view
    cat_lovers = []
    dog_lovers = []
    graph = [[] for _ in range(view)]
    for i in range(view):
        a,b = input().rstrip().split()
        cat_love = a[0] == 'C'
        if a[0] == 'D':
            a,b = b,a
        c = int(a[1:])
        d = int(b[1:])
        if cat_love:
            cat_lovers.append((c,d))
        else:
            dog_lovers.append((c,d))

    n,m = len(cat_lovers), len(dog_lovers)
    for i in range(n):
        for j in range(m):
            c1,d1 = cat_lovers[i]
            c2,d2 = dog_lovers[j]
            if c1 == c2 or d1 == d2:
                graph[i].append(j+n)

    print(view - bimatch())