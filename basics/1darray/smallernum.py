n, x = map(int,input().split())
L = list(map(int,input().split()))
L2 = []
for i in L:
    if i < x:
        L2.append(i)

print(' '.join(map(str,L2)))