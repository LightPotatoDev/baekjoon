import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int,input().split()))
lis = [0 for _ in range(n)]
lds = [0 for _ in range(n)]

for i in range(n):
    arr = [lis[j] for j in range(i) if L[j] < L[i]]
    lis[i] = 1 + max(arr, default=0)

    arr = [lds[j] for j in range(n-i,n) if L[j] < L[n-i-1]]
    lds[n-i-1] = 1 + max(arr, default=0)

lbs = [lis[i]+lds[i]-1 for i in range(n)]
print(max(lbs))