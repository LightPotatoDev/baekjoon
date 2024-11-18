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

while True:
    n = int(input())
    if n == -1:
        break
    M = [[1,1],[1,0]]
    print(matrixExp(M,n,int(1e4))[0][1])