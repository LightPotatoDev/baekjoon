import sys
input = sys.stdin.readline

def ternary_search():
    lo = 0
    hi = int(1e9)
    while hi-lo >= 3:
        mid1 = (2*lo+hi)//3
        mid2 = (lo+2*hi)//3

        if expect(mid1) >= expect(mid2):
            lo = mid1
        elif expect(mid1) < expect(mid2):
            hi = mid2

    return lo+1

def expect(a):
    return (n*a+m) / (1-(1-p/10000)**a)

t = int(input())
for _ in range(t):
    n,m,p = map(int,input().split())
    print(expect(ternary_search()))