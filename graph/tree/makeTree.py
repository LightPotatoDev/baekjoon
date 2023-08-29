n,m = map(int,input().split())

for i in range(n-m):
    print(i,i+1)

for i in range(m-1):
    print(n-m,i+n-m+1)