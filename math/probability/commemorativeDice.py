from fractions import Fraction

D1 = list(map(int,input().split()))
D2 = list(map(int,input().split()))

win = 0

for i in D1:
    for j in D2:
        if i > j:
            win += 1

print(Fraction(win,36))