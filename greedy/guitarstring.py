n,m = map(int,input().split())
pack = 9999
single = 9999

for _ in range(m):
    p,s = map(int,input().split())
    pack = min(pack,p)
    single = min(single,s)

if pack > single*6:
    print(single*n)
else:
    print(min(pack * (n//6) + single * (n%6), pack*(n//6+1)))
