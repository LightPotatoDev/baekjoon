a,b = map(int,input().split())
if b < a:
    b,a = a,b

if a*3 <= b:
    print(a)
elif a/2 >= b/3:
    print(a/2)
else:
    print(b/3)