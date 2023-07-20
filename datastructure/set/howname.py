import sys
input = sys.stdin.readline

n,m = map(int,input().split())

A = set()
B = set()
for _ in range(n):
    A.add(input().rstrip())
for _ in range(m):
    B.add(input().rstrip())

C = sorted(list(A&B))
print(len(C))
for i in C:
    print(i)