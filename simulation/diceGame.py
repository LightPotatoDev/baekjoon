n = int(input())
s1,s2 = 100,100

for _ in range(n):
    a,b = map(int,input().split())
    if a>b:
        s2 -= a
    if b>a:
        s1 -= b

print(s1)
print(s2)