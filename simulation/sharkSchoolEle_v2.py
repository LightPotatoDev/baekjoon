n = int(input())
stud_faves = dict()
stud_order = []
room = [[0]*n for _ in range(n)]

for _ in range(n*n):
    s,a,b,c,d = map(int,input().split())
    stud_order.append(s)
    stud_faves[s] = [a,b,c,d]

dy = [0,-1,0,1]
dx = [1,0,-1,0]

def inbounds(y,x):
    return (0 <= y < n) and (0 <= x < n)

def count_near(y,x,target):
    cnt = 0
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if inbounds(ny,nx) and room[ny][nx] in target:
            cnt += 1
    return cnt

def favorite_near(faves):
    fave_num = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if room[i][j] == 0:
                fave_num[i][j] = count_near(i,j,faves)

    pos = []
    max_fave = 0
    for i in range(n):
        for j in range(n):
            if fave_num[i][j] > max_fave:
                pos = []
                max_fave = fave_num[i][j]
            if fave_num[i][j] == max_fave:
                pos.append((i,j))

    return pos

def most_blanks(pos):
    max_blanks = 0
    p = []
    for y,x in pos:
        cnt = count_near(y,x,[0])
        if cnt > max_blanks:
            p = []
            max_blanks = cnt
        if cnt == max_blanks:
            p.append((y,x))

    return p

def smallest_num(pos):
    return min(pos, key = lambda x:(x[0], x[1]))

for i in range(n*n):
    s = stud_order[i]
    p1 = favorite_near(stud_faves[s])
    p2 = most_blanks(p1)
    y,x = smallest_num(p2)
    room[y][x] = s

def enjoyment():
    ans = 0
    for i in range(n):
        for j in range(n):
            s = room[i][j]
            cnt = count_near(i,j,stud_faves[s])
            if cnt >= 1:
                ans += 10 ** (cnt-1)

    return ans

print(enjoyment())