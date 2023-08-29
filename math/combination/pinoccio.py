import math

l = int(input())
s = input()
ans = 1
for i in ["A","C","G","T"]:
    ans = (ans * s.count(i)) % 1000000007
print(ans)
