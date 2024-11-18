import sys
input = sys.stdin.readline

n,m = map(int,input().split())
left = []
for _ in range(n):
    a,b = map(int,input().split())
    if a > b:
        left.append([b,a])

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
ans = m

for a,b in s_left:
    ans += 2*(b-a)

print(ans)