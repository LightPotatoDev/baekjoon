T = int(input())

def vps(s):
    depth = 0
    for i in s:
        if i == '(':
            depth += 1
        if i == ')':
            depth -= 1
        if depth <= -1:
            return "NO"
    if depth != 0:
        return "NO"
    else:
        return "YES"


for _ in range(T):
    s = input()
    print(vps(s))