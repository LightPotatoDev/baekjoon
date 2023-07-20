T = int(input())
for _ in range(T):
    L = list(map(int,input().split()))[1:]
    avg = sum(L) / len(L)
    cnt = sum(i > avg for i in L)
    print(f"{(cnt * 100 / len(L)):.3f}%")