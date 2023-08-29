n,l = map(int,input().split())
L = list(map(int,input().split()))
L.sort()

for i in L:
    if i <= l:
        l += 1
    else:
        break

print(l)