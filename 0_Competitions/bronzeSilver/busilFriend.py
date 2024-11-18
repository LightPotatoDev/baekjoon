a,b = map(int,input().split())
k,x = map(int,input().split())
ans = 0
for i in range(a,b+1):
    if abs(k-i) <= x:
        ans += 1

if ans != 0:
    print(ans)
else:
    print("IMPOSSIBLE")