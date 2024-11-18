import sys
input = sys.stdin.readline

def matrixMul(A,B,mod=None):
    n = len(A)
    res = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += A[i][k] * B[k][j]

    if mod == None:
        return res

    for i in range(n):
        for j in range(n):
            res[i][j] %= mod

    return res

def matrixExp(A,p,mod=None):
    n = len(A)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        res[i][i] = 1

    while p:
        if p & 1:
            res = matrixMul(A,res,mod)
        A = matrixMul(A,A,mod)
        p >>= 1

    return res

n,m = map(int,input().split())
M = [[0]*n for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    M[a-1][b-1] = 1
    M[b-1][a-1] = 1

d = int(input())
M = matrixExp(M,d,int(1e9)+7)
print(M[0][0])