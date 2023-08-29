n,r = map(int,input().split())

def getDiv(n):
    div = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            div.append(i)
            if i**2 != n:
                div.append(n//i)
    return div

L = getDiv(n-r)
s = 0
for i in L:
    if n % i == r:
        s += i
print(s)