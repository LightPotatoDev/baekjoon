import sys
input = sys.stdin.readline

n = int(input())
balls = [list(map(int,input().split()))+[i] for i in range(n)]
balls.sort(key=lambda x:x[1])
col = [0]*(n+1)
ans = [0]*n
prev_size = -1
same_size = []
total_size = 0

def pop_out():
    global same_size
    global total_size

    for cc,ss,ii in same_size:
        ans[ii] = total_size - col[cc]
    for cc,ss,ii in same_size:
        total_size += ss
        col[cc] += ss
    same_size = []

for c,s,i in balls:
    if s != prev_size:
        pop_out()
        prev_size = s

    same_size.append([c,s,i])

pop_out()
for i in ans:
    print(i)