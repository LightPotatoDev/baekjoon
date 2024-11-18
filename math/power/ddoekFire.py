n = int(input())
if n == 0:
    print(1)
else:
    print(pow(2,n-1,int(1e9)+7))