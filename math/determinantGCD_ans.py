from math import gcd

fibo = [0,1]
mod = int(1e9)+7
for _ in range(int(1e5)):
    fibo.append((fibo[-1]+fibo[-2]) % mod)

n = int(input())
s = 0
for i in range(1,n+1):
    s = (s + fibo[gcd(i+1,n+1)]) % mod
print(s)