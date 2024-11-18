import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    dots = list(map(int,input().split()))
    dots.sort()
    dotSet = set(dots)
    ans = 0

    for i in range(n):
        for j in range(i+1,n):
            a = dots[i]
            c = dots[j]
            if (a+c) % 2 == 1:
                continue
            b = (a+c) // 2
            if b in dotSet:
                ans += 1

    print(ans)