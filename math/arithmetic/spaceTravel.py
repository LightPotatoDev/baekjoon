T = int(input())
for _ in range(T):
    n,d = map(int,input().split())
    cnt = 0
    for _ in range(n):
        v,f,c = map(int,input().split())
        if d <= v * (f/c):
            cnt += 1
    print(cnt)
