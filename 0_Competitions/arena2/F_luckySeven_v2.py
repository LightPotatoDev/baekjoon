T = int(input())

def solve(turn, cur):
    global ans

    if turn == n:
        print(cur)
        if cur == 0:
            ans = "LUCKY"
            return 1
        return 0

    op = Oper[turn]
    v  = Num[turn]

    first  = 7*int(op[0]=="*")+v[0]
    second = 7*int(op[1]=="*")+v[1]
    ret = dp[cur][first][second]

    if ret != -1:
        return ret

    next = [0,0]
    for i in range(2):
        if op[i] == "+":
            next[i] = (cur+v[i])%7
        else:
            next[i] = (cur*v[i])%7

    dp[cur][first][second] = solve(turn+1, next[0]) or solve(turn+1, next[1])
    return dp[cur][first][second]


for _ in range(T):
    n = int(input())
    Oper = []
    Num = []
    dp = [[[-1]*14 for _ in range(14)] for _ in range(7)]
    for _ in range(n):
        op1, v1, op2, v2 = input().split()
        Oper.append((op1,op2))
        Num.append((int(v1)%7, int(v2)%7))

    ans = "UNLUCKY"
    solve(0,1)
    print(ans)

##    for i in dp:
##        for j in i:
##            print(j)
##        print('')
