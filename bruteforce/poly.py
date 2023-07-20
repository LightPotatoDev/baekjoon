def calc(a,b,c,d,e,f):
    for x in range(-999,1000):
        for y in range(-999,1000):
            if a*x + b*y == c and d*x + e*y == f:
                return ' '.join(map(str,[x,y]))

a,b,c,d,e,f = map(int,input().split())
print(calc(a,b,c,d,e,f))