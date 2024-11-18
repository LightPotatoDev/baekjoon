n,m,k = map(int,input().split())
minQ = max(0,n-m*k)
maxQ = max(0,n-m*k+m-1)
print(minQ,maxQ)