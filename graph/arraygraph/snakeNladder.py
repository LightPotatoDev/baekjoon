from collections import deque

n,m = map(int,input().split())
ladders = [tuple(map(int,input().split())) for _ in range(n)]
snakes  = [tuple(map(int,input().split())) for _ in range(m)]

tiles = [0]*101
for i in snakes:
    tiles[i[0]] = -1

dq = deque([1])

def checkladder(position):
    l_starts = [l[0] for l in ladders]
    if position in l_starts:
        ind = l_starts.index(position)
        return ladders[ind][1]
    return 0


while tiles[100] == 0:
    p = dq.popleft()
    for i in range(1,7):
        if p+i <= 100 and tiles[p+i] == 0:
            tiles[p+i] = tiles[p] + 1
            dq.append(p+i)
            l_pos = checkladder(p+i)
            if l_pos != 0:
                tiles[l_pos] = tiles[p] + 1
                dq.append(l_pos)

print(tiles[100])