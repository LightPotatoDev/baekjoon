import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e5)+100)

T = int(input())

def solve(turn, cur):
    global flag

    if flag == 1:
        return

    if turn == n:
        if cur == 0:
            flag = 1
        return

    op = Oper[turn]
    v  = Num[turn]

    for i in range(2):
        next = 0
        if op[i] == "+":
            next = (cur+v[i])%7
        else:
            next = (cur*v[i])%7

        if dp[turn][next] == 1:
            continue

        dp[turn][next] = 1
        solve(turn+1, next)

for _ in range(T):
    n = int(input())
    Oper = []
    Num = []
    dp = [[0]*7 for _ in range(n)]
    for _ in range(n):
        op1, v1, op2, v2 = input().split()
        Oper.append((op1,op2))
        Num.append((int(v1)%7, int(v2)%7))

    flag = 0
    solve(0,1)
    if flag == 0:
        print("UNLUCKY")
    else:
        print("LUCKY")
