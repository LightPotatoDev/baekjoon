import sys
input = sys.stdin.readline

n = int(input())
L = [int(input()) for _ in range(n)]
most = max(L)
A = set(L)
B = set()

for i in range(n):
    for j in range(n):
        if L[i]+L[j] < most:
            B.add(L[i]+L[j])

ans = 0
for i in A:
    for j in A:
        if j-i in B:
            ans = max(ans,i,j)

print(ans)