import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e5))

T = int(input())

def solve(turn, cur):
    global ans

    if turn == n:
        if cur == 0:
            ans = "LUCKY"
            return 1
        return 0

    op = Oper[turn]
    v  = Num[turn]

    for i in range(2):
        next = 0
        if op[i] == "+":
            next = (cur+v[i])%7
        else:
            next = (cur*v[i])%7

        ret = dp[turn][cur][next]
        if ret != -1:
            continue

        dp[turn][cur][next] = solve(turn+1, next)
    return 0

for _ in range(T):
    n = int(input())
    Oper = []
    Num = []
    dp = [[[-1]*7 for _ in range(7)] for _ in range(n)]
    for _ in range(n):
        op1, v1, op2, v2 = input().split()
        Oper.append((op1,op2))
        Num.append((int(v1)%7, int(v2)%7))

    ans = "UNLUCKY"
    solve(0,1)
    print(ans)