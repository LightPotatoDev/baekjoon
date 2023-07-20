a = 1
b = 2
n = int(input())

for i in range(n-2):
    a,b = b,(a+b)%15746

if n == 1:
    print(a)
else:
    print(b)
