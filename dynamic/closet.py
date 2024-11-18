n = int(input())
a,b = map(int,input().split())
a,b = a-1,b-1
q = int(input())
query = [int(input())-1 for _ in range(q)]
dp = [[[int(1e10)]*n for _ in range(n)] for _ in range(q)] #[query][1st hole][2nd hole]
if query[0] != b:
    dp[0][query[0]][b] = abs(query[0]-a)
if query[0] != a:
    dp[0][a][query[0]] = abs(query[0]-b)

for i in range(1,q):
    for j in range(n):
        for k in range(n):
            if dp[i-1][j][k] != -1:
                if query[i] != k:
                    dp[i][query[i]][k] = min(dp[i][query[i]][k],dp[i-1][j][k] + abs(query[i]-j))
                if query[i] != j:
                    dp[i][j][query[i]] = min(dp[i][j][query[i]],dp[i-1][j][k] + abs(query[i]-k))

ans = int(1e10)
for j in range(n):
    for k in range(n):
        ans = min(dp[q-1][j][k],ans)
print(ans)

for i in dp:
    for j in i:
        print(j)
    print('')