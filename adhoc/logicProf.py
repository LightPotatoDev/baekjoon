n = int(input())
L = list(map(int,input().split()))

ans = -1
for i in range(50,-1,-1):
    if L.count(i) == i:
        ans = i
        break

print(ans)