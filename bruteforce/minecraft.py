import sys

n, m, b = map(int,input().split())

L = [0]*257
for _ in range(n):
    for i in list(map(int,sys.stdin.readline().split())):
        L[i] += 1

def totalheight(L):
    total = 0
    for i,x in enumerate(L):
        total += i * x
    return total

targetH = (totalheight(L) + b) // (m*n)
if targetH > 256:
    targetH = 256

times = dict()
while targetH >= 0:
    sec = 0
    for i,x in enumerate(L): #i: height, x: blocknum
        sec += abs(targetH - i) * (int(targetH < i) + 1) * x

    times[targetH] = sec
    targetH -= 1

h_leasttime = [k for k,v in times.items() if v == min(times.values())]
print(times[h_leasttime[0]], h_leasttime[0])