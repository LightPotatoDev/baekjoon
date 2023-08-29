import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    if n <= 2 or m <= 2:
        print("First")
    elif n%2 == 1 and m%2 == 1:
        print("First")
    else:
        print("Second")