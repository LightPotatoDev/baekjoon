m,l = map(int,input().split())
M,L = map(int,input().split())
tm,tl = map(int,input().split())

def cow_crane(pos,m_ok,l_ok):
    t = 0
    tm,tl = 0,0

    for i in range(len(pos)-1):
        d = abs(pos[i+1]-pos[i])
        t += d
        if i == m_ok:
            tm = t
        if i == l_ok:
            tl = t

    return (tm,tl)

times = []
times.append(cow_crane([0,m,M,l,L],1,3))
times.append(cow_crane([0,l,L,m,M],3,1))
times.append(cow_crane([0,m,l,L,l,M],4,2))
times.append(cow_crane([0,l,m,M,m,L],2,4))

ans = 'impossible'
for tmm,tll in times:
    if tmm <= tm and tll <= tl:
        ans = 'possible'
        break
print(ans)