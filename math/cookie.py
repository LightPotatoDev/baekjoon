k,n,m = map(int,input().split())
adding = k*n-m
if adding < 0:
    print(0)
else:
    print(adding)