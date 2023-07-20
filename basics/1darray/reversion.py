N, M = map(int, input().split())
L = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    L[i-1:j] = reversed(L[i-1:j])

print(' '.join(map(str, L)))