import sys
input = sys.stdin.readline

n,b = map(int,input().split())
M = []
for _ in range(n):
    M.append(list(map(int,input().split())))

def elementMul(y,x,A,B):
    total = 0
    for i in range(n):
        total += A[y][i] * B[i][x]
    return total % 1000

def matrixMul(A,B):
    L = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            L[i][j] = elementMul(i,j,A,B)
    return L

leftover = []
while b > 1:
    if b%2 != 0:
        leftover.append(M)
    M = matrixMul(M,M)
    b //= 2

for N in leftover:
    M = matrixMul(M,N)

for row in M:
    row = list(map(lambda x:x%1000, row))
    print(*row)