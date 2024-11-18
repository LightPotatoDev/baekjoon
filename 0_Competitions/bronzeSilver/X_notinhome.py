n,m = map(int,input().split())
t,s = map(int,input().split())

zip = n + ((n-1)//8)*s
dok = t + m + ((m-1)//8)*(s+t*2)
if zip < dok:
    print("Zip")
    print(zip)
else:
    print("Dok")
    print(dok)