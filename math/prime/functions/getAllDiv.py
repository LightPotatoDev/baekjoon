def getAllDiv(n):
    Div = [1]*(n+1)
    for i in range(2,n+1):
        for j in range(i,n+1,i):
            Div[j] += i
    return Div

#합 구하기

def getAllDiv(n):
    Div = [[1] for _ in range(n+1)]
    for i in range(2,n+1):
        for j in range(i,n+1,i):
            Div[j].append(i)
    return Div

#약수 리스트