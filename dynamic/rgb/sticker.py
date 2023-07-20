import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    if n >= 2:
        A[1] = A[1] + B[0]
        B[1] = B[1] + A[0]
    for i in range(2,n):
        A[i] = max(B[i-2],B[i-1]) + A[i]
        B[i] = max(A[i-2],A[i-1]) + B[i]

    print(max(A[-1],B[-1]))