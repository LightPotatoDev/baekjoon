n = int(input())

num = 1
for i in range(1,n+1):
    num *= i

s = str(num)[::-1]

for i,x in enumerate(s):
    if x != "0":
        print(i)
        break