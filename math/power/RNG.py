m,a,c,x0,n,g = map(int,input().split())
b = a-1

A = (x0%m*pow(a,n,m))%m
B = (pow(a,n,b*m)-1%(b*m))%(b*m)
C = ((c%m)*((B//b)%m))%m
print((A+C)%m%g)

aa = x0*pow(a,n)
bb = c*(pow(a,n)-1) // (a-1)
print(A,B,C,aa,bb)