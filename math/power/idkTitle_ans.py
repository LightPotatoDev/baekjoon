n = int(input())
mod = int(1e9)+3

def geometricSum(a,r,n):
    if n == 1:
        return a
    if n%2 == 0:
        return (geometricSum(a,r,n//2) * (1+pow(r,n//2,mod))) % mod
    if n%2 == 1:
        return (geometricSum(a,r,n//2) * (1+pow(r,n//2,mod)) + a*pow(r,n-1,mod)) % mod

if n == 1:
    print(4)
elif n == 2:
    print(12)
else:
    print((4*(pow(3,n-1,mod)-2*geometricSum(3**((n-1)%2),9,(n-1)//2))) % mod)