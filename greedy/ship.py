n = int(input())
limit = [0] + list(map(int,input().split()))
m = int(input())
boxes = list(map(int,input().split()))

limit.sort()
boxes.sort()
if limit[-1] < boxes[-1]:
    print(-1)
    exit()

pickups = [0]*m
cranes = 1
idx = m-1
maxT = 1

while idx >= 0:
    t = 0

    for _ in range(maxT):
        if idx < 0:
            break
        t += 1
        pickups[idx] = t
        idx -= 1

    while idx >= 0 and limit[-cranes-1] < boxes[idx]:
        t += 1
        for _ in range(cranes):
            if idx < 0:
                break
            pickups[idx] = t
            idx -= 1

    cranes += 1
    maxT = max(maxT,t)

print(max(pickups))