import sys
input = sys.stdin.readline

def getDiv(n):
    if n == 1:
        return [1]
    divs = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            divs.append(i)
            if i**2 != n:
                divs.append(n//i)
    divs.sort()
    return divs

numState = [0] * 5001
#0 -부족수 1-완전수 2-과잉수

for i in range(1,5001):
    divSum = sum(getDiv(i)[:-1])
    if divSum < i:
        numState[i] = 0
    elif divSum == i:
        numState[i] = 1
    else:
        numState[i] = 2

T = int(input())
for _ in range(T):
    n = int(input())
    div = getDiv(n)[:-1]
    if numState[n] == 2 and all([numState[i]<=1 for i in div]):
        print("Good Bye")
    else:
        print("BOJ 2022")