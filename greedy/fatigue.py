a,b,c,m = map(int,input().split())

work = 0
fatigue = 0
for _ in range(24):
    if fatigue <= m-a:
        work += b
        fatigue += a
    else:
        fatigue -= c
        if fatigue < 0:
            fatigue = 0

print(work)
