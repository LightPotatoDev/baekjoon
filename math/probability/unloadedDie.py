L = list(map(float,input().split()))
expect = sum([L[i]*(i+1) for i in range(6)])
ans = int(1e10)

for i in range(6):
    if L[i] == 0:
        continue
    changed = (i+1) - (expect-3.5) / L[i]
    ans = min(ans,abs(changed-(i+1)))

print("{:.3f}".format(round(ans,3)))

#print("%.3f" % ans)