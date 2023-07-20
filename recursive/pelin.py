n = int(input())

def isPelindrome(s,l,r,called):
    if l >= r:
        return (1,called)
    elif s[l] != s[r]:
        return (0,called)
    else:
        return isPelindrome(s,l+1,r-1,called + 1)

for _ in range(n):
    s = input()
    output = isPelindrome(s,0,len(s)-1,1)
    print(output[0],output[1])