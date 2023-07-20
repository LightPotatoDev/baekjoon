import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
me = [0,0]
L = []
for i in range(n):
    line = list(input().rstrip())
    if 'I' in line:
        me = [i,line.index('I')]
    L.append(line)

dq = deque() #checklist
dq.append(me)
friends = 0
while dq:
    y,x = dq[0][0], dq[0][1]

    near = [[y-1,x],[y+1,x],[y,x-1],[y,x+1]]
    for i in near:
        inbounds = (-1 < i[0] < n) and (-1 < i[1] < m)
        if inbounds:
            if L[i[0]][i[1]] == 'O' or L[i[0]][i[1]] == 'P':
                dq.append(i)
                if L[i[0]][i[1]] == 'P':
                    friends += 1
                L[i[0]][i[1]] = 'C' #Checked
    dq.popleft()

if friends != 0:
    print(friends)
else:
    print('TT')