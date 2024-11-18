n = int(input())
mod = int(1e6)+3

def geometricSum(a,r,n):
    if n == 1:
        return a
    if n%2 == 0:
        return (geometricSum(a,r,n//2) * (1+pow(r,n//2,mod))) % mod
    if n%2 == 1:
        return (geometricSum(a,r,n//2) * (1+pow(r,n//2,mod)) + a*pow(r,n-1,mod)) % mod

print((pow(2,n-1,mod) * (pow(2,n-1,mod) - 1) - geometricSum(1,4,n-1)) % mod)