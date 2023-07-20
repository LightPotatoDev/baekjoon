n = int(input())
L = []
for _ in range(n):
    L.append(list(map(int,input().split())))
L.sort()
for i in range(n):
    print(' '.join(map(str,L[i])))