def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

a,b = map(int,input().split())
if isPrime(a) and isPrime(a+b*int(1e6)):
    print("Yes")
else:
    print("No")