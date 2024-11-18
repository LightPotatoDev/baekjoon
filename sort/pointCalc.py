L = [(int(input()),i+1) for i in range(8)]
L.sort(reverse=True)

total = 0
ans = []
for i in L[:5]:
    total += i[0]
    ans.append(i[1])
print(total)
ans.sort()
print(*ans)
