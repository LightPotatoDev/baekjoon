n = int(input())

def isHansu(n):
    a = n // 100
    b = (n // 10) % 10
    c = n % 10

    if a == 0 or b-a == c-b:
        return 1
    else:
        return 0

s = 0
for i in range(1,n+1):
    s += isHansu(i)

print(s)