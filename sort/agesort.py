import sys

n = int(input())
L = []

for _ in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    L.append([age,name])

L.sort(key = lambda x:x[0])
for i in L:
    print(' '.join(map(str,i)))