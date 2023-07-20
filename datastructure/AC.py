import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    command = list(input().rstrip())
    n = int(input())
    myinp = input()[1:-2].rstrip().split(',')
    de = deque()
    if len(myinp[0]) != 0:
        de = deque(map(int,myinp))

    popFront = True
    okState = True

    for i in command:
        if i == 'R':
            popFront = not popFront
        elif i == 'D' and de:
            if popFront == True:
                a = de.popleft()
            else:
                a = de.pop()
        else:
            print('error')
            okState = False
            break

    if not okState:
        continue

    if popFront == False:
        de.reverse()

    print('['+','.join(map(str,de))+']')