import sys
input = sys.stdin.readline

L = [1]*1000001
for i in range(2,1000001):
    for j in range(i,1000001,i):
        L[j] += i

for i in range(1000000):
    L[i+1] += L[i]

T = int(input())
for _ in range(T):
    print(L[int(input())]-1)