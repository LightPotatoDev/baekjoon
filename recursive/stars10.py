n = int(input())

L = [['*' for _ in range(n)] for _ in range(n)]

def erase(upperleft,n):
    global L

    start_y = upperleft[0] + n
    start_x = upperleft[1] + n

    for i in range(start_y, start_y+n):
        for j in range(start_x,start_x+n):
            L[i][j] = ' '

    if n == 1:
        return

    for i in range(3):
        for j in range(3):
            erase([upperleft[0]+i*n,upperleft[1]+j*n],n//3)

erase([0,0],n//3)
for i in L:
    print(''.join(i))

""" by freeemily
n=int(input())
z=0
while n>1:
    n/=3
    z+=1

def star(n):
    if n==1:
        return ['***','* *','***']
    else:
        a=star(n-1)
        k=len(a)
        for i in range(1,k+1):
            a.append(str(a[i-1]+' '*3**(n-1)+a[i-1]))
            a[i-1]*=3
        for i in range(1,k+1):
            a.append(a[i-1])
        return a

for i in star(z):
    print(i)
"""