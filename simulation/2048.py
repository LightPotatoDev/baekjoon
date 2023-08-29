import sys
input = sys.stdin.readline
from itertools import product
from copy import deepcopy

n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]

prod = product(range(4), repeat=5)

def getblank(dir,r,c):
    if dir == 0:
        for i in range(n):
            if A[i][c] == 0:
                return (i,c)
    elif dir == 1:
        for j in range(n-1,-1,-1):
            if A[r][j] == 0:
                return (r,j)
    elif dir == 2:
        for i in range(n-1,-1,-1):
            if A[i][c] == 0:
                return (i,c)
    elif dir == 3:
        for j in range(n):
            if A[r][j] == 0:
                return (r,j)

#up:0, right:1, down:2, left:3
def shift(dir):

    def merge(dir,y,x):
        if dir == 0 and y >= 1 and A[y][x] == A[y-1][x]:
            A[y-1][x] *= 2
            A[y][x] = 0
            Merged[y][x] = 1

        elif dir == 1 and x < n-1 and A[y][x] == A[y][x+1]:
            A[y][x+1] *= 2
            A[y][x] = 0
            Merged[y][x] = 1

        elif dir == 2 and y < n-1 and A[y][x] == A[y+1][x]:
            A[y+1][x] *= 2
            A[y][x] = 0
            Merged[y][x] = 1

        elif dir == 3 and x >= 1 and A[y][x] == A[y][x-1]:
            A[y][x-1] *= 2
            A[y][x] = 0
            Merged[y][x] = 1

    Merged = [[0]*n for _ in range(n)]

    Y = []
    X = []
    if dir == 0:
        Y = range(n)
        X = range(n)
    elif dir == 1:
        Y = range(n)
        X = range(n-1,-1,-1)
    elif dir == 2:
        Y = range(n-1,-1,-1)
        X = range(n)
    elif dir == 3:
        Y = range(n)
        X = range(n)

    for i in Y:
        for j in X:
            if A[i][j] != 0:
                num = A[i][j]
                A[i][j] = 0
                y,x = getblank(dir,i,j)
                A[y][x] = num
                if Merged[y][x] == 0:
                    merge(dir,y,x)

ans = 0
for p in prod:
    A = deepcopy(L)
    for i in p:
        shift(i)
    ans = max(ans, max([max(A[i]) for i in range(n)]))
print(ans)

##A = deepcopy(L)
##for i in [1,1,1,1,1]:
##    shift(i)
##    for i in A:
##        print(i)
##    print('')
