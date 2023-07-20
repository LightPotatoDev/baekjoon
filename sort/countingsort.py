import sys

n = int(sys.stdin.readline())
L = [0]*10001

for _ in range(n):
    L[int(sys.stdin.readline())] += 1

myindex = 0
for i in L:
    for _ in range(i):
        print(myindex)
    myindex += 1