n = int(input())
L = list(map(int,input().split()))
stk = []
ans = [0]*n

for i,x in enumerate(L[::-1]):
    while stk and stk[-1][1] < x:
        ans[n-stk[-1][0]-1] = n-i
        stk.pop()
    stk.append((i,x))

print(*ans)