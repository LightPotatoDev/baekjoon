def generate_sequence(n,l,r,x,y,z,b1,b2):
    b = [b1,b2]
    m = 2**32
    for i in range(n-2):
        b.append((b[i]*x + b[i+1]*y + z) % m)
    return b

def mod_sequence(b,r,l):
    a = [0]*len(b)
    for i in range(len(b)):
        a[i] = b[i] % (r-l+1) + l
    return a

n,l,r,x,y,z,b1,b2 = map(int,input().split())
b = generate_sequence(n,l,r,x,y,z,b1,b2)
a = mod_sequence(b,r,l)
print(a)

