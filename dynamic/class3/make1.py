x = int(input())

def makex(x):
    steps = [0] * (x+1)
    for i in range(x-1, -1, -1):
        S = [i*3, i*2, i+1]
        valid_S = [j for j in S if j <= x]
        steps[i] = 1 + min([steps[j] for j in valid_S], default = 0)
    return steps[1]

print(makex(x))

""" by wlem150
T = int(input())
dp = [0] * (T+1)
dp[1] = 0
for i in range(2, T+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[T])
"""