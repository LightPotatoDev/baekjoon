import sys
input = sys.stdin.readline

n,m = map(int,input().split())
meat = [tuple(map(int,input().split())) for _ in range(n)]
meat.sort(key=lambda x:x[1])

cost = [0]*n
weight = [0]*n
wSum = [0]*n

cost[0] = meat[0][1]
weight[0] = meat[0][0]
wSum[0] = weight[0]
ptr = -1
for i in range(1,n):
    w,c = meat[i]
    cost[i] = c
    wSum[i] = wSum[i-1]+w
    if cost[i-1] < c:
        weight[i] = wSum[i-1]+w
        ptr = i-1
    elif cost[i-1] == c:
        if ptr == -1:
            weight[i] = w
        else:
            weight[i] = wSum[ptr] + w

print(meat)
print(cost)
print(weight)
