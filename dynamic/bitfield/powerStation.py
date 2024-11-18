n = int(input())
cost = [list(map(int,input().split())) for _ in range(n)]
is_on_str = input()
is_on = [int(s == 'Y') for s in is_on_str]
p = int(input())

if p <= sum(is_on):
    print(0)
    exit()

INF = int(1e3)
dp = [[INF]*(1<<n) for _ in range(n+1)]

is_on_num = sum([(1<<i) * is_on[i] for i in range(n)])
dp[sum(is_on)][is_on_num] = 0

def power_on(i,j):
    for k in range(n):
        if ((j >> k) & 1) == 0:
            min_cost = INF
            for l in range(n):
                if ((j >> l) & 1) == 1:
                    min_cost = min(min_cost, cost[l][k])
            dp[i+1][j+(1<<k)] = min(dp[i+1][j+(1<<k)], dp[i][j] + min_cost)


for i in range(sum(is_on), n):
    for j in range(1<<n):
        if dp[i][j] != INF:
            power_on(i,j)

ans = min(dp[p])
print(ans if ans != INF else -1)