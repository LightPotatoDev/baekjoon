Prob = list(map(int,input().split()))
n = Prob.pop(0)
Prob = list(map(lambda x:x/100, Prob))
ans = 0

dy = [0,0,1,-1]
dx = [1,-1,0,0]
G = [[0]*29 for _ in range(29)]

def move(p,step,y,x):
    global ans

    if step == n:
        ans += p
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if G[ny][nx] == 0:
            G[ny][nx] = 1
            move(p*Prob[i],step+1,ny,nx)
            G[ny][nx] = 0

G[14][14] = 1
move(1,0,14,14)
print(ans)