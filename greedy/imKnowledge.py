from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
pos = []
neg = []

for _ in range(n):
    a,b = map(int,input().split())
    if a <= b:
        pos.append([a,b])
    else:
        neg.append([a,b])


pos.sort(key=lambda x:(x[0],x[1]))
enjoy = 0
for a,b in pos:
    if a <= enjoy:
        enjoy += b-a
    else:
        print(0)
        exit()

print('idk')