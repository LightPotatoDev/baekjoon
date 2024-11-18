n = int(input())
if n%2 == 1:
    print(0)
else:
    dp = [1]
    for i in range(n//2):
        s = 0
        for j in range(i,-1,-1):
            if j == i:
                s += dp[j]*3
            else:
                s += dp[j]*2
        dp.append(s)
    print(dp[n//2])
