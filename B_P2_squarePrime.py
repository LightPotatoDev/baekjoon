def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def isSquare(n):
    return (n >= 0) and (int(n**0.5)**2 == n)

def P2(A):
    n = len(A)
    s = 0
    for i in range(n):
        if isPrime(i) and isSquare(A[i]):
            s += A[i]
    return s

############### SUBMIT THE CODE ABOVE ONLY ###############

print(P2([0, 100, 20, 100, 40]))
print(P2([-100,99999,-123,100,100])) # 100
