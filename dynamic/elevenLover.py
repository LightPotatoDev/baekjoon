import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()
    if n[0] == '0':
        break
    l = list(map(int,n))[::-1]
    dp = [[[0]*11 for _ in range(len(l))] for _ in range(2)] #[+,-][digit][mod]
    ans = 0
    for i in range(len(l)-1):
        dp[0][i][l[i]] += 1
        for j in range(11):
            dp[1][i+1][(j-l[i+1])%11] += dp[0][i][j]
            dp[0][i+1][(j+l[i+1])%11] += dp[1][i][j]
        if l[i] != 0:
            ans += dp[0][i][0] + dp[1][i][0]

    if l[len(l)-1] != 0:
        ans += dp[0][len(l)-1][0] + dp[1][len(l)-1][0]

    print(ans)
