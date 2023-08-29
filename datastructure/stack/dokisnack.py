n = int(input())
L = list(map(int,input().split()))

stk = []
cnt = 1
for i in L:
    if i == cnt:
        cnt += 1
    else:
        stk.append(i)

if stk[::-1] == [i for i in range(cnt,n+1)]:
    print("Nice")
else:
    print("Sad")
print(cnt,stk[::-1],[i for i in range(cnt,n+1)])
