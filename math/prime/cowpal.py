def getDiv(n):
    if n == 1:
        return 0
    divSum = 1
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            divSum += i
            if i**2 != n:
                divSum += n//i
    return divSum

divs = [0]*50001
for i in range(1,50001):
    divs[i] = getDiv(i)

s = int(input())
while True:
    a = divs[s]
    b = divs[a]
    if s == b and a != b:
        print(s,a)
        break
    s += 1