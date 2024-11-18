import sys
input = sys.stdin.readline

T = int(input())

for i in range(1,T+1):
    print(f"Scenario #{i}:")
    L = list(map(int,input().split()))
    L.sort()
    a,b,c = L
    if a**2 + b**2 == c**2:
        print("yes")
    else:
        print("no")
    print('')