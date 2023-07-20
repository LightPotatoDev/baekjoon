import sys
input = sys.stdin.readline

n = int(input())
dist = [0] + list(map(int,input().split()))
price = list(map(int,input().split()))

for i in range(1,n):
    dist[i] += dist[i-1]

def findcheap(start, curprice):
    next = 0
    while start+next < n-1:
        next += 1
        if price[start+next] < curprice:
            break
    return next

pos = 0
cost = 0
while pos < n-1:
    move = findcheap(pos,price[pos])
    cost += (dist[pos+move] - dist[pos]) * price[pos]
    pos += move
print(cost)