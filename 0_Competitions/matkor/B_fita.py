def isSquare(n):
    if n < 0:
        return False
    return int(n**0.5)**2 == n

n = int(input())

if isSquare(n):
    print(-1)
    exit()

cnt = 0
a = 1
while a <= int(n**0.5):
    b = n-a**2
    if isSquare(b):
        cnt += 1
        if a**2 == b:
            cnt += 1
    a += 1
cnt //= 2

def getDiv(n):
    div = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            div.append(i)
            div.append(n//i)
    return div

N = getDiv(n)
for i in range(len(N)//2):
    if (N[2*i]+N[2*i+1])%2 == 0:
        cnt += 1
print(cnt)