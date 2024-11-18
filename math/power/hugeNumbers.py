import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    a,n,p = map(int,input().split())
    ans = 1
    for i in range(1,n+1):
        ans = (ans * pow(a,i,p)) % p

    print(f"Case #{tc+1}: {ans}")