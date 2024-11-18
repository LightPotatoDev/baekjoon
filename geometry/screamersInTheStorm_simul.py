from itertools import product

def distance(p):
    n = len(p)
    s = sum([p[i]**2 for i in range(n)]) ** (0.5)
    return s

def abs_sum(p):
    return sum([abs(i) for i in p])

def screamer(d,r):
    points = product(list(range(-10,11)), repeat=d)
    s = 0
    for p in points:
        dist = distance(p)
        if dist <= r:
            s += abs_sum(p)
    return s

for d in range(1,5):
    for r in range(1,6):
        print(d,r,screamer(d,r))