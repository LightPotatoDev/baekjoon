import sys
input = sys.stdin.readline
n = int(input())

S = set()
cnt = 0
for _ in range(n):
    s = input().rstrip()
    if s == 'ENTER':
        cnt += len(S)
        S = set()
    else:
        S.add(s)

cnt += len(S)
print(cnt)