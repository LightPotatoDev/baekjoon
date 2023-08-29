n = int(input())
dp = [[int(1e7),-1] for _ in range(n+1)]
dp[-1] = [0,-1]

for i in range(n,0,-1):
    if i%3 == 0:
        dp[i//3] = min([dp[i][0]+1,i], dp[i//3])
    if i%2 == 0:
        dp[i//2] = min([dp[i][0]+1,i], dp[i//2])
    dp[i-1] = min([dp[i][0]+1,i],dp[i-1])

trace = [1]
back = 1
while back != -1:
    trace.append(dp[back][1])
    back = dp[back][1]
trace.pop()
print(dp[1][0])
print(*trace[::-1])