T = int(input())

for t in range(1,T+1):
    k,v = map(int,input().split())
    col = (v+1)**3
    dupe = v**3
    if k < v:
        print(0)
    else:
        print(f"Case #{t}: {col*(k-v+1) - dupe*(k-v)}")