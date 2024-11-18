n,x = map(int,input().split())

if (26*n < x or x < n):
    print('!')
    exit(0)

aTimes = (26*(n-1)-x+26) // 25
middle = 25 * aTimes + x - 26*(n-1)
zTimes = max(0,n-aTimes-1)

if aTimes == n:
    print('A'*n)
else:
    print('A'*aTimes + chr(middle+64) + 'Z'*zTimes)