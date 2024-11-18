import sys
input = sys.stdin.readline



def matrixAdd(A,B):
    n = len(A)
    res = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            res[i][j] = (A[i][j] + B[i][j]) % mod

    return res

def matrixMul(A,B):
    n = len(A)
    res = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += A[i][k] * B[k][j]

    for i in range(n):
        for j in range(n):
            res[i][j] %= mod

    return res

def matrixExp(A,p):
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

def matrixExpSum(A,p):
    if p == 1:
        return A

    if p % 2 == 0:
        return matrixMul(matrixExpSum(A,p//2),matrixAdd(I,matrixExp(A,p//2)))

    if p % 2 == 1:
        return matrixMul(matrixExpSum(A,p//2),matrixAdd(I,matrixExp(A,p//2)))


mod = 1000
n,b = map(int,input().split())
I = [[0]*n for _ in range(n)]
for i in range(n):
    I[i][i] = 1

