v,w,d = map(int,input().split())

dist = 0
collision = 0
while True:
    dist += 5*(w/v)**2
    if dist > d:
        break
    collision += 1
    v *= 0.8

print(collision)
