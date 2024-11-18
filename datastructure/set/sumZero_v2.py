import sys
input = sys.stdin.readline

n = int(input())
L = [[] for _ in range(4)]
for _ in range(n):
    A = map(int,input().split())
    for i,x in enumerate(A):
        L[i].append(x)

D = dict()
ans = 0

for i in L[0]:
    for j in L[1]:
        if i+j not in D:
            D[i+j] = 1
        else:
            D[i+j] += 1

for i in L[2]:
    for j in L[3]:
        if -i-j in D:
            ans += D[-i-j]
print(ans)