a,b,c = map(int,input().split())

def power(a,b):
    if b == 1:
        return a % c
    if b%2 == 0:
        return (power(a,b//2) * power(a,b//2)) % c
    elif b%2 == 1:
        return (power(a,(b-1)//2) * power(a,(b-1)//2) * a) % c

print(power(a,b) % c)