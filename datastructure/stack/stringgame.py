import sys
input = sys.stdin.readline

a = list(input().rstrip())
aR = a[::-1]
l = len(a)
t = input().rstrip()
stk1 = []
stk2 = []

n = int(input())
c = 0
cmd = [input().rstrip() for _ in range(n)]

i = 0
j = len(t)-1

while i <= j and c < n:
    mode = cmd[c]
    while mode == 'L' and i <= j:
        stk1.append(t[i])
        i += 1

        if len(stk1) >= l and stk1[-l:] == a:
            c += 1
            for _ in range(l):
                stk1.pop()
            break

    while mode == 'R' and i <= j:
        stk2.append(t[j])
        j -= 1

        if len(stk2) >= l and stk2[-l:] == aR:
            c += 1
            for _ in range(l):
                stk2.pop()
            break

while i <= j:
    stk2.append(t[j])
    j -= 1

res = ''.join(stk1) + ''.join(stk2[::-1])

while stk2:
    p = stk2.pop()
    stk1.append(p)
    if len(stk1) >= l and stk1[-l:] == a:
        c += 1
        for _ in range(l):
            stk1.pop()
        if c == n:
            res = ''.join(stk1) + ''.join(stk2[::-1])

ans = ''.join(stk1)
if c < n:
    res = ans

print(min(c,n))
print(res)
if res == ans:
    print("Perfect!")
else:
    print("You Lose!")
