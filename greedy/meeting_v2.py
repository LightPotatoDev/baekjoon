import sys
input = sys.stdin.readline

n = int(input())
L = []
timetable = []
for _ in range(n):
    L.append(tuple(map(int,input().split())))

L.sort(key = lambda x:(x[1],-x[0]))

def caninsert(new):
    old = timetable[-1]
    inside = (old[0] <= new[0] < old[1]) or (old[0] < new[1] <= old[1])
    outside = (new[0] < old[0]) and (new[1] > old[1])
    if inside or outside:
        return False
    return True

timetable.append(L[0])
for new in L[1:]:
    if caninsert(new):
        timetable.append(new)

print(len(timetable))