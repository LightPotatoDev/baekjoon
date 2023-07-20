import math

n = int(input())

dp = [0] * (n+1)

for i in range(1, n+1):
    checklist = [j for j in range(int(math.sqrt(i)), math.ceil(math.sqrt(i/4))-1, -1)]
    num = []
    for j in checklist:
        sub = i - j**2
        if sub == 0:
            num.append(1)
            break
        else:
            num.append(dp[sub]+1)
            if dp[sub]+1 == 2:
                break
    dp[i] = min(num)

print(dp[n])