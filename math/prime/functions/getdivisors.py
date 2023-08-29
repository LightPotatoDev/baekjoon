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

#약수의 합 구하기 (자신 제외)

def getDiv(n):
    div = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            div.append(i)
            if i**2 != n:
                div.append(n//i)
    return div

#약수 리스트 구하기