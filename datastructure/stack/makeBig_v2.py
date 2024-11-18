n,k = map(int,input().split())
s = list(map(int,input()))
stk = []

for i in s:
    while stk and k > 0 and stk[-1] < i:
        stk.pop()
        k -= 1
    stk.append(i)

while k > 0:
    stk.pop()
    k -= 1
print(''.join(map(str,stk)))