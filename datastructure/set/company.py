import sys
input = sys.stdin.readline

n = int(input())
S = set()
for _ in range(n):
    name, act = input().split()
    if act == 'enter':
        S.add(name)
    else:
        S.remove(name)

S = sorted(list(S),reverse=True)
for i in S:
    print(i)