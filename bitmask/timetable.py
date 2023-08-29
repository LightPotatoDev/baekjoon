import sys
input = sys.stdin.readline
mask = 2**50-1

def setKthBit(n,k):
    pos = 2**49 >> (k-1)
    return (pos | n)

n = int(input())
Class = []
for _ in range(n):
    a = 0
    Times = list(map(int,input().split()))[1:]
    for i in Times:
        a = setKthBit(a,i)
    Class.append(a)

m = int(input())
for _ in range(m):
    a = 0
    Available = list(map(int,input().split()))[1:]
    for i in Available:
        a = setKthBit(a,i)
    cnt = 0
    for c in Class:
        cnt += int(((c^mask)|a) == mask)
    print(cnt)

for i in Class:
    print(i,end= ' ')
print('')
for i in Class:
    print(bin(i)[2:].zfill(50), end=' ')