import sys
input = sys.stdin.readline

n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]
L.sort(key=lambda x:x[0])

stk1 = []
stk2 = []
for l,h in L:
    while stk1 and stk1[-1][1] < h:
        stk1.pop()
    stk1.append([l,h])

for l,h in L[::-1]:
    while stk2 and stk2[-1][1] < h:
        stk2.pop()
    stk2.append([l,h])

ans = stk1[0][1] + stk2[0][1]
for i in range(len(stk1)-1):
    ans += stk1[i+1][1] * (stk1[i+1][0] - stk1[i][0])
for i in range(len(stk2)-1):
    ans += stk2[i+1][1] * (stk2[i][0] - stk2[i+1][0])

ans -= stk1[0][1]*(stk2[0][0]-stk1[0][0]+1)

print(ans)