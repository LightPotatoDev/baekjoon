import sys
input = sys.stdin.readline

n = int(input())
L = []

for _ in range(n):
    A = input().rstrip().split()
    for i in range(1,4):
        A[i] = int(A[i])
    L.append(A)

L.sort(key = lambda x:(-x[1],x[2],-x[3],x[0]))
for i in range(n):
    print(L[i][0])