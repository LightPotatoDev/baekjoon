N, M = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(N)]
b = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    L = []
    for j in range(M):
        L.append(a[i][j] + b[i][j])
    print(' '.join(map(str,L)))