n,m = map(int,input().split())
mod = int(1e9)+7

print((pow(m,n,mod) - pow(m-1,n,mod))%mod)