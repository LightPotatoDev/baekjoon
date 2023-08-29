s = input()
num = 0
for i in s:
    if i.isUpper:
        num += ord(i)-38
    else:
        num += ord(i)-96

def sieve(n):
    p = 2
    prime = [1 for i in range(n+1)]
    while p**2 <= n:
        i = p
        while i <= n-p:
            i += p
            prime[i] = 0
        p += 1

    return prime

isPrime = sieve(1040)
if isPrime[num] == 1:
    print("It is a prime word.")
else:
    print("It is not a prime word.")
