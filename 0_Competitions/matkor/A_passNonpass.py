import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    print("swimming", end=' ')
sys.stdout.flush()

Fail = list(input().split())
for i in Fail:
    if i == "bowling":
        print("soccer", end=' ')
    else:
        print("bowling", end=' ')
sys.stdout.flush()