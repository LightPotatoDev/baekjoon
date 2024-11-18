import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    L = list(map(int,input().split()))
    L.sort()
    a,b,c = L
    ans = "NO"
    if a**2 + b**2 == c**2:
        ans = "YES"
    print(f"Case #{tc}: {ans}")