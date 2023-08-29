from collections import deque

def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

n = int(input())

if isPrime(n) == False:
    print("no")
    exit()

dq = deque()
for i in str(n):
    if i == "3" or i == "4" or i == "7":
        print("no")
        exit()
    elif i == "6":
        dq.appendleft("9")
    elif i == "9":
        dq.appendleft("6")
    else:
        dq.appendleft(i)

rev = int(''.join(dq))
if isPrime(rev) == False:
    print("no")
else:
    print("yes")
