import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
m = int(input())

L = list(map(int,input().split()))
for x in L:
    a = x
    for i in range(n):
        if A[i] == 0:
            a,B[i] = B[i],a
    print(a,end=" ")