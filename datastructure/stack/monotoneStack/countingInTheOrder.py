n = int(input())
heights = list(map(int,input().split()))
directions = input()
ans = [0]*n

stk = []
for i,h in enumerate(heights):
    if directions[i] == 'L':
        ans[i] = len(stk)
    while stk and stk[-1] < h:
        stk.pop()
    stk.append(h)

stk = []
for i in range(n-1,-1,-1):
    h = heights[i]
    if directions[i] == 'R':
        ans[i] = len(stk)
    while stk and stk[-1] < h:
        stk.pop()
    stk.append(h)

print(*ans)