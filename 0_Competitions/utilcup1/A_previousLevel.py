n = int(input())
L = list(map(int,input().split()))
lim = (250,275,300,301)

ans = []
for i in L:
    for j in range(4):
        if i < lim[j]:
            ans.append(4-j)
            break
print(*ans)