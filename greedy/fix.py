n,l = map(int,input().split())
L = list(map(int,input().split()))
L.sort()

pos = 0
cnt = 0
for i in L:
    if i >= pos:
        cnt += 1
        pos = i+l

print(cnt)