def getDigit(x):
    minDigit = 10
    maxDigit = 0
    while x > 0:
        if x%10 != 0:
            minDigit = min(x%10,minDigit)
        maxDigit = max(x%10,maxDigit)
        x //= 10
    return (minDigit, maxDigit)

dp = [0]*1000001
for i in range(1,10):
    dp[i] = 1
for i in range(10,1000001):
    mini, maxi = getDigit(i)
    dp[i] = 1-min(dp[i-mini], dp[i-maxi])

g = int(input())
for _ in range(g):
    n = int(input())
    if (dp[n] == 0):
        print("NO")
    else:
        print("YES")