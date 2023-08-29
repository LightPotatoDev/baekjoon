def EEA(a,b):
    if b == 0:
        return (a,(1,0))
    ret = EEA(b,a%b)
    g = ret[0]
    x,y = ret[1]
    return (g,(y,x-(a//b)*y))

print(EEA(6,8))

#ax+by = g
#g = gcd
#returns (g, (x,y))

def modInverse(a,mod):
    ret = EEA(a,mod)
    if ret[0] > 1:
        return -1
    return ret[1][0] % mod

print(modInverse(3,4))
#(a*?)%n = 1