import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
A = []
for _ in range(m):
    a,b = map(int,input().split())
    A.append([a,b-1])

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

connection = sweeping(A)
ans = 0
if connection:
    ans += connection[0][0] - 1
    for i in range(len(connection)-1):
        a,b = connection[i][1], connection[i+1][0]
        ans += b-a-1
    ans += n - connection[-1][1] - 1
    ans += 1
else:
    ans = n
print(ans)