form = input()
d = int(1e9)+9
ans = 1
c = 0
state = ""
for i in form:
    if i == "c":
        if state == "d":
            c = 0
        ans = (ans * (26 - c)) % d
        c = 1
    else:
        if state == "c":
            c = 0
        ans = (ans * (10 - c)) % d
        c = 1
    state = i

print(ans)
