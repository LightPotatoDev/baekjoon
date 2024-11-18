n = int(input())
quests = [tuple(map(int,input().split())) for _ in range(n)]
dp = [[-1 for _ in range(1001)] for _ in range(1001)] #[STR][INT]
dp[1][1] = 0

ans = 0
def complete_quests(char_s,char_i):
    global ans
    pnt = 0
    completed = 0

    for s,i,p in quests:
        if (s <= char_s) or (i <= char_i):
            pnt += p
            completed += 1

    pnt = pnt - (char_s-1) - (char_i-1)
    ans = max(ans,completed)
    return pnt

for i in range(1,1001):
    for j in range(1,1001):
        if dp[i][j] != -1:
            pnt = complete_quests(i,j)
            for k in range(pnt+1):
                ni = min(i + pnt - k,1000)
                nj = min(j + k, 1000)
                dp[ni][nj] = 0

print(ans)
