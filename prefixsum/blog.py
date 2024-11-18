n,k = map(int,input().split())
L = [0]+list(map(int,input().split()))
for i in range(n):
    L[i+1] += L[i]

ans = -100000
days = 0

for i in range(k,n+1):
    num = L[i]-L[i-k]
    if num > ans:
        days = 1
        ans = num
    elif num == ans:
        days += 1

if ans == 0:
    print('SAD')
else:
    print(ans)
    print(days)