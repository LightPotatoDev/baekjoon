import sys
input = sys.stdin.readline

n = int(input())
L = [int(input()) for _ in range(n)]
stk = []
for i in L:
    while stk and stk[-1] <= i:
        stk.pop()
    stk.append(i)
print(len(stk))