import math

n = int(input())
mod = 10007

if n <= 3:
    print(0)
    exit()

ans = 0
for i in range(n//4):
    pickFour = math.comb(13,i+1)
    pickRem  = math.comb(48-4*i,n-4*(i+1))
    ans += ((-1)**(i)) * ((pickFour * pickRem))

print(ans%mod)