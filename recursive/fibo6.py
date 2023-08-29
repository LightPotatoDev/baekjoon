import sys
input = sys.stdin.readline

n = int(input())
M = [[1,1],[1,0]]

def elementMul(y,x,A,B):
    total = 0
    for i in range(2):
        total += A[y][i] * B[i][x]
    return total % 1000000007

def matrixMul(A,B):
    L = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            L[i][j] = elementMul(i,j,A,B)
    return L

leftover = []
while n > 1:
    if n%2 != 0:
        leftover.append(M)
    M = matrixMul(M,M)
    n //= 2

for N in leftover:
    M = matrixMul(M,N)

print(M[0][1])