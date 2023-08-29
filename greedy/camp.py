c = 0
while True:
    c += 1
    l,p,v = map(int,input().split())
    if l == 0:
        break

    adding = 0
    if v%p > l:
        adding = l
    else:
        adding = v%p
    print(f"Case {c}: {(v//p)*l + adding}")