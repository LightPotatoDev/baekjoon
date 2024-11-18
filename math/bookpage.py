n = int(input())

def countDigits(n):
    #0
    cnt = 0
    for i in range(1,11):
        cnt += ((n//10**i-1)*(10**(i-1)) + min(n%10**i+1,10**(i-1))) * int(n>=10**i)
    print(cnt, end = ' ')

    #1-9
    for i in range(1,10):
        cnt = 0
        for j in range(1,11):
            m = n+(10-i)*10**(j-1)
            cnt += ((m//10**j-1)*(10**(j-1)) + min(m%10**j+1,10**(j-1))) * int(m>=10**j)
        print(cnt, end = ' ')


countDigits(n)
#print(countOneSum(b)-countOneSum(a-1))