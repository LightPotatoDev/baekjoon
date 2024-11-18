import sys
input = sys.stdin.readline

n = int(input())
stk = []
score = 0

for _ in range(n):
    hw = list(map(int,input().split()))
    if hw[0] == 1:
        stk.append([hw[1],hw[2]])
    if stk:
        stk[-1][1] -= 1
        if stk[-1][1] == 0:
            score += stk[-1][0]
            stk.pop()
print(score)