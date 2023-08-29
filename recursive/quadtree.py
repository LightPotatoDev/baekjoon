n = int(input())
L = [list(map(int,input())) for _ in range(n)]

def quadtree(y,x,n): #top left

    total = 0
    for i in range(y,y+n):
        for j in range(x,x+n):
            total += L[i][j]
    if total == 0 or total == n**2:
        print(total // (n**2),end = '')
        return

    print("(",end = '')
    quadtree(y,x,n//2)
    quadtree(y,x+n//2,n//2)
    quadtree(y+n//2,x,n//2)
    quadtree(y+n//2,x+n//2,n//2)
    print(")",end = '')

quadtree(0,0,n)

