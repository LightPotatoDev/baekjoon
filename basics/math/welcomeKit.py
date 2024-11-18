n = int(input())
L = list(map(int,input().split()))
t,p = map(int,input().split())

ans = 0
for i in L:
    ans += (i-1)//t + 1
print(ans)

print(n//p, n%p)