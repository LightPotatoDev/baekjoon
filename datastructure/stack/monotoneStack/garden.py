import sys
input = sys.stdin.readline

n = int(input())
L = [int(input()) for _ in range(n)]+[int(1e10)]
stk = []
ans = [0]*n

for i,x in enumerate(L):
    while stk and stk[-1][1] <= x:
        ans[stk[-1][0]] = i-stk[-1][0]-1
        stk.pop()
    stk.append((i,x))

print(sum(ans))