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
    print(ans[:10])
print(max(ans))

#dp[i] = max(dp[i - 1], max(dp[i - 2], dp[i - 3] + A[i - 1]) + A[i]);