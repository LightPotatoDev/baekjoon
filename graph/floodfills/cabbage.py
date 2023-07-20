T = int(input())

def deploy(L,coord,m,n):
    checklist = [coord]
    while len(checklist) > 0:
        y,x = checklist[0][0], checklist[0][1]
        L[y][x] = 0
        near = [[y-1,x],[y+1,x],[y,x-1],[y,x+1]]
        for i in near:
            inbounds = (-1 < i[0] < n) and (-1 < i[1] < m)
            if inbounds and L[i[0]][i[1]] == 1 and i not in checklist:
                checklist.append(i)
        checklist.pop(0)
    return L

for _ in range(T):
    m,n,k = map(int,input().split()) #m:가로, n:세로
    L = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        L[y][x] = 1 #L[세로위치][가로위치]

    worms = 0
    for i in range(m):
        for j in range(n):
            if L[j][i] == 1: #j:세로, i:가로
                L = deploy(L,[j,i],m,n)
                worms += 1

    print(worms)

"""from cls1230
graph = [[0]*N for _ in range(M)]    # (x, y) 좌표 개념과 M행 N열 개념이 반대이므로 그래프를 전치
q = deque()                          # deque의 popleft 사용하면 수행속도 빠름
q.append((a, b))                     # 큐에 좌표값 추가
"""