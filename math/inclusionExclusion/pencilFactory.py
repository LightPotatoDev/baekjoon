import math
n,m,k = map(int,input().split())
period = math.lcm(n+1,m+1)
nothing = k // period
unpaint = k // (n+1) - nothing
unvarnish = k // (m+1) - nothing
complete = k - nothing - unpaint - unvarnish
print(complete, nothing, unvarnish, unpaint)