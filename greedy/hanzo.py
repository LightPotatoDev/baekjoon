n = int(input())
L = list(map(int,input().split())) + [100001]

best = 0
cnt = 0
maxCnt = 0
for i in L:
    if i > best:
        maxCnt = max(maxCnt, cnt)
        cnt = 0
        best = i
    else:
        cnt += 1

print(maxCnt)
