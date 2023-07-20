n = int(input())

L = [0]
for _ in range(n):
    L.append(int(input()))

dp = [[0,0]]*(n+1) #[1,2,4,6],[1,2,5,6] (마지막 1연속,2연속)
dp[1] = [L[1],L[1]]
if n >= 2:
    dp[2] = [L[1]+L[2],L[1]+L[2]]
if n >= 3:
    dp[3] = [L[1]+L[3],L[2]+L[3]]
if n >= 4:
    dp[4] = [dp[2][0]+L[4], dp[3][0]+L[4]]

for i in range(5,n+1):
    dp[i] = [max(dp[i-2][0],dp[i-2][1])+L[i], max(dp[i-1][0], dp[i-4][1]+L[i-1])+L[i]]

print(max(dp[n-1][0],dp[n-1][1],dp[n][0],dp[n][1]))

""" by duiyang2030

n = int(input())
org = [0] * 10000
ans = [0] * 10000
for i in range(n):
    org[i] = int(input())

ans[0] = org[0]
ans[1] = org[0] + org[1]
ans[2] = max(ans[1], org[2]+org[1], org[2]+org[0])
for j in range(3, n):
    ans[j] = max(ans[j-1], org[j]+org[j-1]+ans[j-3], org[j]+ans[j-2])
print(max(ans))

"""