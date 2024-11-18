import sys
input = sys.stdin.readline

n,l = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]
ans = 0

def putSlope(A,B,i,diff):
    if (diff == 1):
        start = A[i]
        for j in range(i,i-l,-1):
            if j < 0:
                return 0
            if A[j] != start:
                return 0
            if B[j] == 1:
                return 0
            B[j] = 1

    if (diff == -1):
        start = A[i+1]
        for j in range(i+1, i+l+1, 1):
            if j >= n:
                return 0
            if A[j] != start:
                return 0
            if B[j] == 1:
                return 0
            B[j] = 1

    return B

def checkSlope(A):
    B = [0]*n
    for i in range(n-1):
        diff = A[i+1] - A[i]
        if (diff > 1 or diff < -1):
            return 0
        if (diff == 1 or diff == -1):
            B = putSlope(A,B,i,diff)
            if B == 0:
                return 0
    return 1

for i in range(n):
    ans += checkSlope(L[i])
    ans += checkSlope([L[j][i] for j in range(n)])

print(ans)