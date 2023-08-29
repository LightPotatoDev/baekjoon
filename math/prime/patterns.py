n,k = map(int,input().split())

def getDiv(n):
    if n == 1:
        return 1
    num = 0
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            num += 1
            if i**2 != n:
                num += 1
    return num

L = [0] + [getDiv(i) for i in range(1,n**2+1)]
for i in range(n):
    for j in range(1,n+1):
        if L[i*n+j] <= k:
            print("*",end="")
        else:
            print(".",end="")
    print('')