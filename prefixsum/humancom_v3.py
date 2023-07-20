import sys
input = sys.stdin.readline

s = input().rstrip()
q = int(input())
L = [[0 for _ in range(26)]]
A = [0 for _ in range(26)]
for i,x in enumerate(s):
    A[ord(x)-97] += 1
    L.append(A[:])
L.append(A[:])

for _ in range(q):
    a,l,r = input().split()
    l = int(l)
    r = int(r)
    ans = L[r+1][ord(a)-97] - L[l][ord(a)-97]
    print(ans)
