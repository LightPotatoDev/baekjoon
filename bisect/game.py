x,y = map(int,input().split())

z = (y*100) // x

if z >= 99:
    print(-1)
    exit()

def binsearch():
    lo = 0
    hi = int(1e9)

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        winrate = ((y+mid)*100) // (x+mid)

        if winrate <= z:
            lo = mid
        else:
            hi = mid

    return hi

print(binsearch())