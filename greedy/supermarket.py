import sys
input = sys.stdin.readline

n = int(input())
L = [tuple(map(int,input().split())) for _ in range(n)]
L.sort(reverse = True)
schedule = [0]*10001

for i in range(n):
    money,day = L[i]
    idx = day
    while schedule[idx] != 0:
        idx -= 1
    if idx >= 1:
        schedule[idx] = money

print(sum(schedule))