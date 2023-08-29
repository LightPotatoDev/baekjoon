n = int(input())

s1 = "* "*((n+1)//2)
s2 = " *"*(n//2)

for i in range(n):
    print(s1)
    if n != 1:
        print(s2)