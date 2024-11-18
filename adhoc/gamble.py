n = int(input())
ans = 0
for _ in range(2):
    ans += sum(list(map(lambda x:abs(int(x)), input().split())))
print(ans)