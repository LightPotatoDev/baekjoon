n = int(input())
m = int(input())
graph = [[] for _ in range(4)]
dp = [[0]*4 for _ in range(n+1)]
dp[0] = [0.25]*4

for _ in range(m):
    s,e,p = input().split()
    graph[ord(s)-65].append((float(p),ord(e)-65))

for i in range(n):
    for start in range(4):
        for p,end in graph[start]:
            dp[i+1][end] += dp[i][start]*p

for i in dp[n]:
    print(i*100)