a,b = map(int,input().split())

def countOneSum(n):
    #0부터 n까지, i번째 비트가 켜지는 횟수
    ones = 0
    for i in range(54):
        c = (n//(2**(i+1))) * 2**i
        d = (n%(2**(i+1))) - 2**i + 1
        d = d * int(d>=0)
        ones += c+d

    return ones

print(countOneSum(b)-countOneSum(a-1))