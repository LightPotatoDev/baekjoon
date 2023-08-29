s = input()

state = "A"
time = 0
for i in s:
    d = abs(ord(i)-ord(state))
    time += min(d,26-d)
    state = i
print(time)
