n,m = map(int,input().split())
ans = 1
for _ in range(n):
    a = int(input())
    if a != 0:
        ans = (ans*a)%m
print(ans%m)