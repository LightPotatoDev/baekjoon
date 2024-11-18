l,u = map(int,input().split())

def countDigits(n):
    L = [0]*10
    n = max(0,n)
    #0
    cnt = 0
    for i in range(1,11):
        cnt += ((n//10**i-1)*(10**(i-1)) + min(n%10**i+1,10**(i-1))) * int(n>=10**i)
    L[0] = cnt

    #1-9
    for i in range(1,10):
        cnt = 0
        for j in range(1,11):
            m = n+(10-i)*10**(j-1)
            cnt += ((m//10**j-1)*(10**(j-1)) + min(m%10**j+1,10**(j-1))) * int(m>=10**j)
        L[i] = cnt

    return L

def getSum(L):
    s = 0
    for i,x in enumerate(L):
        s += i*x
    return s

A,B = countDigits(l-1),countDigits(u)
print(getSum(B)-getSum(A))