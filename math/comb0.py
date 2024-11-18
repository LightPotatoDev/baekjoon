n,m = map(int,input().split())

def findFactor(n,search):
    cnt = 0
    i = search
    while i <= int(2e9):
        cnt += n // i
        i *= search
    return cnt

fives = findFactor(n,5)-findFactor(n-m,5)-findFactor(m,5)
twos = findFactor(n,2)-findFactor(n-m,2)-findFactor(m,2)
print(min(fives,twos))