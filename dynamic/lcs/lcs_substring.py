s1 = input()
s2 = input()

def lcs_substring(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + 1

    return max([max(r) for r in dp])

print(lcs_substring(s1,s2))