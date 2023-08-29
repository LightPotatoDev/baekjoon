n = int(input())
Y = list(map(int,input().split()))
D = list(map(int,input().split()))

for i in range(1,n//2):
    Y[i] += i
    Y[n-i-1] += i
    D[i] += i
    D[n-i-1] += i
Y[n//2] += n//2
D[n//2] += n//2

L = Y+D
L.sort()
mid = L[n]
if mid < n//2:
    mid = n//2
cnt = 0
for i in L:
    cnt += abs(mid-i)

print(cnt)