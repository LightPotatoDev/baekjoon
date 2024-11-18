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

d = int(input())

M = [[0]*8 for _ in range(8)]
edges = [[0,1],[0,2],[1,2],[1,3],[2,3],[3,4],[3,5],[2,5],[4,5],[4,6],[5,7],[6,7]]
for a,b in edges:
    M[a][b] = 1
    M[b][a] = 1

M = matrixExp(M,d,int(1e9)+7)
print(M[0][0])