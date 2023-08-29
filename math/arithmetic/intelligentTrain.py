ans = 0
cnt = 0
for _ in range(10):
    a,b = map(int,input().split())
    cnt += b-a
    ans = max(ans,cnt)
print(ans)