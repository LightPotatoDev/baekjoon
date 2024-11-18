import sys
input = sys.stdin.readline

n = int(input())
L = [int(input()) for _ in range(n)]
stk = []
ans = 0

for i in L:
    while stk and stk[-1][0] < i:
        stk.pop()
        ans += 1

    same = 0
    if stk and stk[-1][0] == i:
        same = stk[-1][1]+1
    ans += same
    if stk and stk[0][0] != i:
        ans += 1
    stk.append([i,same])

print(ans)