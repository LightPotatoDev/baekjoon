s = list(map(int,list(input())))

zeroOne = [0,0]
state = s[0]
zeroOne[state] = 1

for i in s:
    if i != state:
        state = i
        zeroOne[state] += 1

print(min(zeroOne))
