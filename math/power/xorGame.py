a,b,n = map(int,input().split())
print(pow(2**31,n-1,int(1e9)+7))