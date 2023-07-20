a,b = map(int,input().split())

def gcd(a, b):
    if b > a:
        a, b = b, a
    while a%b != 0:
        a, b = b, a%b
    return(b)

lcm = a*b//gcd(a,b)
print(lcm)

""" by jhshin0904
def lcd(a, b):
    if b > a:
        a, b = b, a
    while a%b != 0:
        a, b = b, a%b
    return(b)

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(a*b//lcd(a, b))
"""

"""by syun9274
import math

a, b = map(int, input().split())
print(f'{math.lcm(a, b)}')
"""