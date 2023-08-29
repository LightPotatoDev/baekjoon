a,b = map(int,input().split())
n = int(input())

favoPress = 0
for _ in range(n):
    favo = int(input())
    if abs(b-a) > abs(b-favo):
        a = favo
        favoPress = 1

print(abs(b-a)+favoPress)