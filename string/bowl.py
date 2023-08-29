S = input()
state = ""

h = 0
for i in S:
    if i != state:
        state = i
        h += 10
    else:
        h += 5

print(h)