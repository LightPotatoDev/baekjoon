from copy import deepcopy
import sys
input = sys.stdin.readline

n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]
mask = 2**n-1

dy = [-1,0,1,0,0]
dx = [0,1,0,-1,0]
def switch(y,x):
    for i in range(5):
        ny = y+dy[i]
        nx = x+dx[i]

        if 0 <= ny < n and 0 <= nx < n:
            A[ny][nx] = 1-A[ny][nx]

ans = int(1e5)
for choice in range(mask+1):
    cnt = 0
    A = deepcopy(L)
    for i in range(n):
        if ((choice >> i) & 1) == 1:
            switch(0,i)
            cnt += 1

    for i in range(1,n):
        for j in range(n):
            if A[i-1][j] == 1:
                switch(i,j)
                cnt += 1

    if all([i == 0 for i in A[n-1]]):
        ans = min(ans, cnt)

if ans == int(1e5):
    print(-1)
else:
    print(ans)