def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def numGen(num,digit):
    if isPrime(num) == False:
        return
    if digit == n:
        print(num)
        return

    num *= 10
    for i in range(10):
        if digit != 0 or i != 0:
            numGen(num+i, digit+1)

n = int(input())
numGen(0,0)