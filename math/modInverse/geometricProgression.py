r,n = map(int,input().split())

b = r-1
a = 1
m = int(1e9)+7

if (r == 1):
    print((a*n)%m)
    exit(0)

B = (pow(r,n,b*m)-1%(b*m))%(b*m)
C = ((a%m)*((B//b)%m))%m

print(C%m)