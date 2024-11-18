import sys
input = sys.stdin.readline

f,r = map(int,input().split())
n = int(input())
c = int(input())
odd = False
if n%2 == 1:
    n += 1
    odd = True
graph = [[0]*(n) for _ in range(n)]
total = 0
for _ in range(c):
    a,b,m = map(int,input().split())
    graph[a-1][b-1] += m
    graph[b-1][a-1] += m
    total += m

def fill_dp(i,j):
    for u in range(n):
        for v in range(u+1,n):
            if graph[u][v] == 0:
                continue
            target = (1 << u) + (1 << v)
            if j & target > 0:
                continue
            if dp[i][j] + graph[u][v] > dp[i+1][target+j]:
                dp[i+1][target+j] = dp[i][j] + graph[u][v]
                bt[i+1][target+j] = j

dp = [[0]*(1<<n) for _ in range(n//2+1)]
bt = [[0]*(1<<n) for _ in range(n//2+1)]
for i in range(n//2):
    for j in range(1<<n):
        if j.bit_count() % 2 == 0:
            fill_dp(i,j)

ans = dp[n//2][2**n-1]

trace = (1<<n)-1
print((total-ans)*r + ans*f)

print_count = 0
printed = [0]*n
for i in range(n//2,-1,-1):
    nxt = bt[i][trace]
    diff = trace - nxt
    pair = []
    for j in range(n):
        if (diff >> j) & 1 == 1:
            pair.append(j+1)
    if len(pair) == 2 and (odd == False or not (n in pair)):
        print(*pair)
        print_count += 1
        printed[pair[0]-1] = 1
        printed[pair[1]-1] = 1
    trace = nxt

a = 0
for i in range(n):
    if print_count >= n//2:
        break
    if printed[i] == 0:
        if a == 0:
            a = i+1
        else:
            print(a,i+1)
            print_count += 1
            a = 0