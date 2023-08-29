n = int(input())
f = int(input())
if n >= 100:
    n = (n // 100) * 100

r = n % f
plus = f-r
if plus == f:
    print("00")
else:
    print(str(plus)[-2:].zfill(2))