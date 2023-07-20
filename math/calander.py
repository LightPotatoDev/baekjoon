import math

T = int(input())

for i in range(T):
    m,n,x,y = map(int,input().split())
    l = math.lcm(m,n)
    a = x
    flag = False
    while a <= l:
        if a % n == y % n:
            print(a)
            flag = True
            break
        a += m
    if flag == False:
        print(-1)
