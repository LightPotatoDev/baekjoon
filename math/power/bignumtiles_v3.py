a,b,c = map(int,input().split())

def power(a,b):
    ans = 1
    while b > 0:
        if b % 2 != 0:
            ans = (ans * a) % c
        a = (a**2) % c
        b //= 2
    return ans

print(power(a,b) % c)