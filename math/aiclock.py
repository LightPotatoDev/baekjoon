a,b,c = map(int,input().split())
d = int(input())

exceed = (c+d) // 60
b += exceed
c = (c+d) % 60

exceed2 = b // 60
a += exceed2
b = b % 60

a %= 24
print(a,b,c)