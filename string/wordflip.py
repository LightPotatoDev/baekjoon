T = int(input())

for _ in range(T):
    S = list(input().split())
    for s in S:
        print(s[::-1], end=' ')