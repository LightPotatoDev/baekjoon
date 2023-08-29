n = int(input())

standard = input()
l = len(standard)
ans = list(standard)
for _ in range(n-1):
    s = input()
    for i in range(l):
        if s[i] != standard[i]:
            ans[i] = "?"

print(''.join(ans))