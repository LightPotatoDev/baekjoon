n = int(input())

L = [[' '] * (n-i-1) + ['*'] * (2*i+1) + [' '] * (n-i-1) for i in range(n)]

def erase(upleft,n):
    starty = n + upleft[0]
    startx = 2*n + int(n%3!=0) + upleft[1]

    for i in range(n):
        for j in range(i-n, n-i-1):
            L[starty+i][startx+j] = ' '

    if n == 1:
        return

    erase([upleft[0],upleft[1]+n],n//2)
    erase([upleft[0]+n,upleft[1]],n//2)
    erase([upleft[0]+n,upleft[1]+2*n],n//2)


erase([0,0],n//2)

for i in L:
    print(''.join(i))
