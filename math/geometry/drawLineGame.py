import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    if n <= 1:
        print(1,0)
    else:
        print(0,1)