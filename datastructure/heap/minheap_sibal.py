import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
de = deque()

def insertData(de, x):
    de.append(x)
    pos = len(de)
    while pos > 1:
        if de[pos//2-1] > x:
            de[pos//2-1],de[pos-1] = de[pos-1],de[pos//2-1]
            pos //= 2
        else:
            break
    return de

def deleteData(de):
    print(de.popleft())
    if len(de) == 0:
        return de

    x = de.pop()
    de.appendleft(x)
    pos = 1
    while True:
        if len(de) <= pos*2-1:
            break

        leftNode = de[pos*2-1]
        rightNode = -1
        if len(de) > pos*2:
            rightNode = de[pos*2]

        if leftNode < x and (leftNode < rightNode or rightNode == -1):
            de[pos-1], de[pos*2-1] = de[pos*2-1],de[pos-1]
            pos *= 2
        elif rightNode != -1 and rightNode < x:
            de[pos-1], de[pos*2] = de[pos*2],de[pos-1]
            pos = pos*2 + 1
        else:
            break

    return de

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(de) == 0:
            print(0)
        else:
            de = deleteData(de)
    else:
        de = insertData(de,x)