k = int(input())
dir = []
length = []

for _ in range(6):
    d,l = map(int,input().split())
    dir.append(d)
    length.append(l)

maxind = length.index(max(length))
maxind2 = 0
if length[(maxind+1)%6] > length[(maxind-1)%6]:
    maxind2 = (maxind+1)%6
else:
    maxind2 = (maxind-1)%6

minind = (maxind+3)%6
minind2 = (maxind2+3)%6

print((length[maxind] * length[maxind2] - length[minind] * length[minind2]) * k)