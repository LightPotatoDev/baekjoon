n = int(input())
cur = list(map(int,input().split()))
target = list(map(int,input().split()))

diff = [cur[i]-target[i] for i in range(n)]

def getRange(start,num):
    for i in range(start,n):
        if num > 0 and diff[i] <= 0:
            return range(start,i)
        if num < 0 and diff[i] >= 0:
            return range(start,i)
    return range(start,n)

ans = 0
for i in range(n):
    while diff[i] != 0:
        s = diff[i]
        for j in getRange(i,s):
            if s > 0:
                diff[j] -= 1
            if s < 0:
                diff[j] += 1
        ans += 1

print(ans)