import math

T = int(input())

for _ in range(T):
    h, w, n = map(int,input().split())
    floor = n%h
    room = str(math.ceil(n/h))
    if floor == 0:
        floor = h
    if len(room) == 1:
        room = "0" + room
    print(str(floor)+room)