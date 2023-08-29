T = int(input())

def solve(turn, cur):
    global ans

    if turn == n:
        if cur == 0:
            ans = "LUCKY"
            return 1
        return 0

    opers = Oper[turn]
    vals  = Num[turn]

    for i in range(2):
        opType = int(opers[i]=="*")
        ret = dp[cur][opType][vals[i]]
        if ret != -1:
            return ret
        elif opType == 0:
            dp[cur][opType][vals[i]] = solve(turn+1, (cur+vals[i])%7)
            return ret
        else:
            dp[cur][opType][vals[i]] = solve(turn+1, (cur*vals[i])%7)
            return ret


for _ in range(T):
    n = int(input())
    Oper = []
    Num = []
    dp = [[[-1]*7 for _ in range (2)] for _ in range(7)]
    for _ in range(n):
        op1, v1, op2, v2 = input().split()
        Oper.append((op1,op2))
        Num.append((int(v1)%7, int(v2)%7))

    ans = "UNLUCKY"
    solve(0,1)
    print(ans)

    print(dp)
