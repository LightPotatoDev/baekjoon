n = int(input())
L = list(map(int,input().split()))
L.sort()

ans = 0
for i in L:
    if i-1 > ans:
        break
    else:
        ans += i

print(ans+1)