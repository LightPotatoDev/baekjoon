import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))

m,k = map(int,input().split())
B = []
for _ in range(m):
    B.append(list(map(int,input().split())))

C = [[0]*k for _ in range(n)]

def matrixMul(y,x):
    total = 0
    for i in range(m):
        total += A[y][i] * B[i][x]
    return total

for i in range(n):
    for j in range(k):
        C[i][j] = matrixMul(i,j)

for row in C:
    print(*row)