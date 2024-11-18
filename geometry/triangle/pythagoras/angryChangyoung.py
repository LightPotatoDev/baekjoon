n,w,h = map(int,input().split())
maxL = int((w**2+h**2)**0.5)

for _ in range(n):
    l = int(input())
    if l <= maxL:
        print("DA")
    else:
        print("NE")