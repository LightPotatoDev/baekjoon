import sys
input=sys.stdin.readline

def power(a,n):
    if n==1:
        return a
    elif n%2==0:
        return power(multi(a,a),n//2)
    else:
        return multi(power(a,n-1),a)

def multi(a,b):
    temp=[[len(b[0])]*2 for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            sum=0
            for k in range(len(a[0])):
                sum+=a[i][k]*b[k][j]
            temp[i][j]=sum%mod
    return temp

a,r,n,mod=map(int,input().split())

ans=[[0]*2 for _ in range(2)]
ans[0][0]=1
ans[0][1]=a
ans[1][1]=r

start=[[1,a], [0,r]]

if n==1:
    print(a%mod)
elif n==2:
    print((a+a*r)%mod)
else:
    print(multi(power(ans,n-1),start)[0][1])


