n = int(input())
towers = list(map(int,input().split()))
towers.sort()

DP_SIZE = 500001
dp = [[0]*DP_SIZE for _ in range(n)]

GO_UP = 1
STOP = 2 #include self
GO_LEFT_UP = 3 #include self

dp[0][towers[0]] = STOP
for i in range(1,n):
    for j in range(DP_SIZE):
        if j == towers[i]:
            dp[i][j] = STOP
        elif j-towers[i] > 0 and dp[i-1][j-towers[i]] != 0:
            dp[i][j] = GO_LEFT_UP
        elif dp[i-1][j] != 0:
            dp[i][j] = GO_UP

def backtrace(i,j,already_exists):
    exists = [0]*n
    while dp[i][j] != STOP:
        if dp[i][j] == GO_UP:
            i -= 1
        elif dp[i][j] == GO_LEFT_UP:
            if already_exists != -1 and already_exists[i] == 1:
                return -1
            exists[i] = 1
            j -= towers[i]
            i -= 1
    exists[i] = 1
    if already_exists != -1 and already_exists[i] == 1:
        return -1
    return exists

for j in range(DP_SIZE-1,-1,-1):
    state = 0
    already_exists = []
    for i in range(n):
        if state == 0:
            if dp[i][j] == STOP or dp[i][j] == GO_LEFT_UP:
                already_exists = backtrace(i,j,-1)
                state = 1

        elif state == 1:
            if dp[i][j] == STOP or dp[i][j] == GO_LEFT_UP:
                if backtrace(i,j,already_exists) != -1:
                    print(j)
                    exit()

print(-1)