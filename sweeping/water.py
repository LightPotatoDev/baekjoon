import sys
input = sys.stdin.readline

n,m = map(int,input().split())
left = []
right = []
for _ in range(n):
    a,b = map(int,input().split())
    if a > b:
        left.append([b,a])
    else:
        right.append([a,b])

def sweeping(A):
    A.sort(key = lambda x:(x[0],x[1]))
    s,e = -int(1e10), -int(1e10)
    lines = []
    for i in range(len(A)):
        new_line = False
        a,b = A[i]
        if e < a:
            s = a
            new_line = True
        e = max(e,b)
        if new_line:
            lines.append([s,e])
        if lines:
            lines[-1][1] = e

    return lines

s_left = sweeping(left)
s_right = sweeping(right)
ans = m
max_r = 0
min_l = m

for a,b in s_left:
    if b <= m:
        ans += 2*(b-a)
    else:
        min_l = min(min_l, a)
        max_r = max(max_r, b)

for a,b in s_right:
    max_r = max(max_r,b)

ans += 2*(max_r-m)
ans += 2*(m-min_l)
print(ans)