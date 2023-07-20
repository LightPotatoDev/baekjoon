from collections import deque
n,m = map(int,input().split())
L = list(map(int,input().split()))
de = deque()
for i in range(n):
    de.append(i+1)

cnt = 0
for i in L:
    pos = de.index(i)
    if pos <= len(de) // 2: #shift_left
        for _ in range(pos):
            a = de.popleft()
            de.append(a)
        cnt += pos
    else:
        for _ in range(len(de)-pos): #shift_right
            a = de.pop()
            de.appendleft(a)
        cnt += len(de) - pos
    de.popleft()

print(cnt)

#  de.rotate(-1) : shift_left
#  de.rotate(1)  : shift_right