import math
import sys
input = sys.stdin.readline
from copy import deepcopy

MAXPOW = math.ceil(math.log(32000,2))

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

def matrixExp(A,mod=None):
    n = len(A)
    res = deepcopy(A)

    while n:
        if n & 1:
            res = matrixMul(A,res,mod)
        A = matrixMul(A,A,mod)
        n >> 1

    return res


while True:
    n,m,p = map(int,input().split())

    if n == 0:
        break

    M = [list(map(int,input().split())) for _ in range(n)]
    ans = [[0]*n for _ in range(n)]
    for i in range(n):
        ans[i][i] = 1
    Msquared = []

    for i in range(MAXPOW):
        Msquared.append(deepcopy(M))
        M = deepcopy(matrixMul(M,M,m))

    for i in range(MAXPOW):
        if ((p >> i) & 1) == 1:
            ans = deepcopy(matrixMul(ans,Msquared[i],m))

    for row in ans:
        print(*row)
    print('')
