def calc_time(c):
    s = 0
    for i in range(n):
        if speed[i]+c == 0:
            return 1e10
        s += dist[i] / (speed[i]+c)
    print(s)
    return s

def binsearch():
    lo = -1e6
    hi = 1e6

    while abs(lo-hi) > 1e-7:
        mid = (lo + hi) / 2

        if calc_time(mid) > t:
            lo = mid
        else:
            hi = mid
        print(lo,hi)
    return hi

n,t = map(int,input().split())
dist = []
speed = []
for _ in range(n):
    d,s = map(int,input().split())
    dist.append(d)
    speed.append(s)

print(binsearch())