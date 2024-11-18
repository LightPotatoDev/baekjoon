x,y = map(int,input().split())
r = int(input())

dx = [1,1,-1,-1]
dy = [1,-1,-1,1]
for i in range(4):
    print(x+dx[i]*r, y+dy[i]*r)