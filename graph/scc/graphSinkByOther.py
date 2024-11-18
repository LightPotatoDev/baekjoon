import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = int(1e6)

def scc(node):
    global ids, scc_cnt
    ids_arr[node], parents[node] = ids, ids
    ids += 1; visited[node] = True
    stack.append(node)

    for now in graph[node]:
        if ids_arr[now] == 0:
            scc(now)
            parents[node] = min(parents[now], parents[node])
        elif visited[now]:
            parents[node] = min(parents[now], parents[node])

    w = -1
    if parents[node] == ids_arr[node]:
        while w != node:
            w = stack.pop()
            scc_idx[w] = scc_cnt
            visited[w] = False
        scc_cnt += 1

while True:
    x = input().rstrip()
    if x == '0': break
    v, e = map(int, x.split())
    if e == 0:
        input();print(*[i for i in range(1, v+1)])
    else:
        l = list(map(int, input().split()))
        graph = [[] for _ in range(v+1)]
        for i in range(0, e*2-1, 2):
            graph[l[i]].append(l[i+1])
        stack = []
        visited = [False]*(v+1)
        ids, ids_arr = 1, [0]*(v+1)
        parents, scc_idx, scc_cnt = [0]*(v+1), [-1]*(v+1), 0
        #scc_idx: i번째 노드는 scc_idx[i]번째 scc에 속해 있음

        for i in range(1, v+1):
            if ids_arr[i] == 0: scc(i)
        ans = set([i for i in range(scc_cnt)])
        for i in range(1, v+1):
            for j in graph[i]:
                if scc_idx[i] != scc_idx[j]:
                    if scc_idx[i] in ans:
                        ans.remove(scc_idx[i])
        ans2 = []
        for i in range(1, v+1):
            if scc_idx[i] in ans:
                ans2.append(i)
        print(*ans2)

        #https://www.acmicpc.net/source/64753680