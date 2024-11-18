n,k = map(int,input().split())
L = list(map(int,input().split()))
plug = [0]*n
ans = 0

def calc_cost(idx,start,elec):
    if plug[idx] == 0:
        return 0
    cost = 0
    for i in range(start,n):
        if

for i,x in enumerate(L):
    plugging = -1
    mincost = 900
    for j in range(n):
        cost = calc_cost(j,i,x)
        if cost < mincost:
            mincost = cost
            plugging = j
    if plug[pluggging] != x and plug[plugging] != 0:
        ans += 1
    plug[plugging] = x

print(ans)
