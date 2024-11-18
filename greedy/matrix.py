import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = [list(map(int,list(input().rstrip()))) for _ in range(n)]
B = [list(map(int,list(input().rstrip()))) for _ in range(n)]

def change(y,x):
    for i in range(3):
        for j in range(3):
            A[y+i][x+j] = 1-A[y+i][x+j]

ans = 0
for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            change(i,j)
            ans += 1

for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            print(-1)
            exit()

print(ans)