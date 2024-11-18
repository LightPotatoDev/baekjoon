n,k = map(int,input().split())
minBall = k*(k+1)//2
if n < minBall:
    print(-1)
else:
    print(k-int(n%k==minBall%k))